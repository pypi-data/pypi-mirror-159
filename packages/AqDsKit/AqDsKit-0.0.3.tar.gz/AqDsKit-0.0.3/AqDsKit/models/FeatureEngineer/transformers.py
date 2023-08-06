from typing import Union
import logging
import pandas as pd
import numpy as np
from functools import partial
from sklearn.experimental import enable_iterative_imputer
from scipy.special import softmax
from sklearn.ensemble import RandomForestRegressor
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import VarianceThreshold, mutual_info_classif, mutual_info_regression, SelectPercentile, SelectFromModel, SelectorMixin
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.impute import SimpleImputer, IterativeImputer, KNNImputer
from sklearn.preprocessing import StandardScaler, RobustScaler, OneHotEncoder, FunctionTransformer, normalize, scale
from sklearn.utils.validation import check_is_fitted

from category_encoders.ordinal import OrdinalEncoder
from category_encoders.count import CountEncoder

from AqDsKit.models.FeatureEngineer.featureHelper import FeatureMeta
from AqDsKit.models.utils.checks import check_params
from AqDsKit.models.utils.support import make_present_col_selector

class WeightedAverager(BaseEstimator, TransformerMixin):
    def __init__(self, weights, intercept: float = 0.0, n_jobs: int = -1):
        """calculate weighted average value using given weight vector

        :param weights: 1D array-like or iterables of length n_features
        :param intercept: the intercept to use, default is 0.0
        :param n_jobs:
        """
        self.weights = np.asarray(weights)
        self.intercept = intercept
        self.n_jobs = n_jobs
        self.lm_ = LinearRegression(fit_intercept=False, n_jobs=n_jobs)
        self.lm_.coef_ = np.array([self.weights, ])  # use 2D coef to make prediction output 2D
        self.lm_.intercept_ = [intercept, ]  # no intercept required

    @property
    def averager_(self):
        return self.lm_

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return self.lm_.predict(X)

class FeatureNorm(BaseEstimator, TransformerMixin):
    def __init__(self, method: str = 'l1'):
        """normalize features along axis = 1

        :param method: {'l1', 'l2', 'softmax', 'standard'}, default to l1
            -- l1: use simple sum to normalize, the transformed will have .sum(axis = 1) = 1
            -- l2, use l2 norm to normalize, i.e., keep the angle and shrink the length of the feature, the transformed will have .squared.sum(axis = 1)
            -- softmax, apply logistic function to each feature to impose positive features, i.e., exp(Fi) / sum(exo(F)), the transformed will have .sum(axis = 1) = 1
            -- standard, apply standard scaler, i.e., will center and scale
        """
        self.method = check_params(method, allowed_values = ['l1', 'l2', 'softmax', 'standard'])

    def fit(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            self.feature_names_in_ = np.array(X.columns)

        return self

    def get_feature_names_out(self, input_features=None):
        if input_features is not None:
            if len(self.feature_names_in_) != len(input_features):
                raise ValueError(
                    f"Length of input_features is {len(input_features)} while expected len(self.feature_names_in_)")
        else:
            input_features = self.feature_names_in_

        return np.asarray(input_features)

    def transform(self, X):
        if self.method in ['l1', 'l2']:
            X_ = normalize(X, norm = self.method, axis = 1, return_norm = False)
        elif self.method == 'softmax':
            X_ = softmax(X, axis = 1)
        elif self.method == 'standard':
            X_ = scale(X, axis = 1)

        if hasattr(self, 'feature_names_in_'):
            return pd.DataFrame(X_, columns = self.feature_names_in_)
        else:
            return X_


class MyImputer(SimpleImputer):
    def transform(self, X):
        X_ = super().transform(X)

        if self.add_indicator:
            # indicator for categorical variables will be bool format (True/False), convert it to int 0/1
            missing_indicator_indices = self.indicator_.features_ + len(self.feature_names_in_)
            X_[:, missing_indicator_indices] = X_[:, missing_indicator_indices].astype('int')

        columns = self.get_feature_names_out()
        return pd.DataFrame(X_, columns=columns)

    def get_feature_names_out(self, input_features=None):
        if input_features is not None:
            if len(self.feature_names_in_) != len(input_features):
                raise ValueError(
                    f"Length of input_features is {len(input_features)} while expected len(self.feature_names_in_)")
        else:
            input_features = self.feature_names_in_

        if self.add_indicator:
            prefix = "_naFlag"
            missing_indicator_indices = self.indicator_.features_
            missing_indicators = [input_features[idx] + prefix for idx in missing_indicator_indices]
            transformed_colnames = list(input_features) + missing_indicators
        else:
            transformed_colnames = list(input_features)

        return np.array(transformed_colnames)


class BucketCategValue(BaseEstimator, TransformerMixin):
    def __init__(self, cols, threshold : float = 'auto', replace : bool = True, new_cols = None): # no *args or **kwargs
        """Reduce the number of values in given categorical variable, i.e., combine rare categories into 'Other' group

        :param cols: array-like, list of categorical columns to perform the value bucketing
        :param threshold: a float number between 0-1, default 'auto' and will find best splitting threshold
        :param replace: will replace original column if replace = True, otherwise a new column will be created
        :param new_cols: the new columns names, only effective when replace = False

        threshold should be a value between 0-1, will merge small categories so that count(small_categ) / count(*) <= threshold
        """
        self.cols = cols
        self.threshold = threshold
        self.replace = replace
        self.new_cols = new_cols

    def fit(self, X, y = None):
        if isinstance(X, pd.DataFrame):
            self.feature_names_in_ = np.array(X.columns)

        self.tiny_cols = {}
        for c in self.cols:
            col = X[c]

            if self.threshold != 'auto':
                freq_df = pd.DataFrame({
                    'rev_cum_freq' : col.value_counts()[::-1].cumsum()[::-1].shift(-1),
                    'freq' : col.value_counts()
                })
                rev_cum_freqs = freq_df[freq_df.rev_cum_freq < freq_df.freq]
                if len(rev_cum_freqs) < len(col.value_counts()) * 0.2:
                    logging.warning(f'threshold is set to auto, but the labels are too evenly distributed, failed to find a splitting point for col {c}, will use 0.8 as default threshold')
                    cum_freqs = col.value_counts(normalize = True).cumsum()
                    self.tiny_cols[c] = cum_freqs[cum_freqs > 0.8].index
                else:
                    splitting_v = rev_cum_freqs.iloc[0]['freq']
                    freqs = col.value_counts()
                    self.tiny_cols[c] = freqs[freqs < splitting_v].index
            else:
                # threshold should be a value between 0-1, will merge small categories so that count(small_categ) / count(*) <= threshold
                cum_freqs = col.value_counts(normalize = True).cumsum()
                self.tiny_cols[c] = cum_freqs[cum_freqs > self.threshold].index

        return self  # nothing else to do

    def transform(self, X, y = None):
        X = X.copy()
        for i, c in enumerate(self.cols):
            if self.replace:
                X.loc[X[c].isin(self.tiny_cols[c]), c] = 'Other'
            else:
                new_col = self.new_cols[i]
                X.loc[X[c].isin(self.tiny_cols[c]), new_col] = 'Other'
                X.loc[~X[c].isin(self.tiny_cols[c]), new_col] = X.loc[~X[c].isin(self.tiny_cols[c]), c]
        return X

    def get_feature_names_out(self, input_features=None):
        if input_features:
            if hasattr(self, 'feature_names_in_'):
                if len(self.feature_names_in_) != len(input_features):
                    raise ValueError(f"Length of input_features is {len(input_features)} while expected len(self.feature_names_in_)")
            return input_features
        else:
            if hasattr(self, 'feature_names_in_'):
                return self.feature_names_in_
            else:
                raise AttributeError("Has no attribute feature_names_in_, please use pd.DataFrame when training /testing")

# Inspired from stackoverflow.com/questions/25239958
class MostFrequentImputer(BaseEstimator, TransformerMixin):
    '''Impute null values with most frequent value for categorical variable(s)'''
    def fit(self, X, y = None):
        self.most_frequent_ = pd.Series(
            [X[c].value_counts().index[0] for c in X],
            index = X.columns
        )
        return self

    def transform(self, X, y = None):
        return X.fillna(self.most_frequent_)


def find_num_features(X):
    if isinstance(X, pd.Series):
        return 1
    else:
        if len(X.shape) == 1:
            return 1
        else:
            return X.shape[1]

class OutlierClipper(BaseEstimator, TransformerMixin):
    def __init__(self, strategy: str = "iqr", quantile_range: tuple = (5, 95), constant_capper: tuple = None):
        """clip the numerical feature into specified range or statistically based range

        :param strategy: {'iqr' for IQR cut, 'quantile' for given quantile clip, 'constant' for constant value clip}
        :param quantile_range: a tuple of low and high quantile threshold, use when strategy = 'quantile'
        :param constant_capper: a tuple of constant low and high threshold, use when strategy = 'constant'
        """
        self.strategy = check_params(strategy, allowed_values = ['iqr', 'quantile', 'constant'])
        self.quantile_range = quantile_range
        if strategy == 'constant' and constant_capper is None:
            raise ValueError("Must pass constant_capper (tuple) if strategy is set to 'constant'")
        self.constant_capper = constant_capper

    def fit(self, X, y = None):
        if isinstance(X, pd.DataFrame):
            self.feature_names_in_ = np.array(X.columns)
            X = X.values.astype('float')

        if isinstance(X, pd.Series):
            X = X.values.astype('float')

        if self.strategy == 'iqr':
            q1, q3 = np.percentile(X[~np.isnan(X).any(axis=1)], [25, 75], axis = 0)
            iqr = q3 - q1
            self.lower_bound_, self.upper_bound_ = q1 - (1.5 * iqr), q3 + (1.5 * iqr)
        elif self.strategy == 'quantile':
            self.lower_bound_, self.upper_bound_ = np.percentile(X[~np.isnan(X).any(axis=1)], self.quantile_range, axis = 0)
        elif self.strategy == 'constant':
            if find_num_features(X) > 1:
                raise ValueError("If strategy is set to 'constant', can only accept array with only 1 column")
            else:
                self.lower_bound_, self.upper_bound_ = self.constant_capper
        return self

    def transform(self, X, y = None):
        X = X.copy()
        if isinstance(X, np.ndarray):
            n, m = X.shape
            if m == 1:
                if isinstance(self.lower_bound_, (list, np.ndarray)):
                    self.lower_bound_ = self.lower_bound_[0]
                    self.upper_bound_ = self.upper_bound_[0]
                X[:, 0] = np.clip(X[:, 0], self.lower_bound_, self.upper_bound_)
            else:
                for j in range(m):
                    X[:, j] = np.clip(X[:, j], self.lower_bound_[j], self.upper_bound_[j])
        elif isinstance(X, pd.DataFrame):
            n, m = X.shape
            if m == 1:
                if isinstance(self.lower_bound_, (list, np.ndarray)):
                    self.lower_bound_ = self.lower_bound_[0]
                    self.upper_bound_ = self.upper_bound_[0]
                X.iloc[X.iloc[:, 0] < self.lower_bound_, 0] = self.lower_bound_
                X.iloc[X.iloc[:, 0] > self.upper_bound_, 0] = self.upper_bound_
            else:
                for j in range(m):
                    X.iloc[X.iloc[:, j] < self.lower_bound_[j], 0] = self.lower_bound_[j]
                    X.iloc[X.iloc[:, j] > self.upper_bound_[j], 0] = self.upper_bound_[j]

        elif isinstance(X, pd.Series):
            if isinstance(self.lower_bound_, (list, np.ndarray)):
                self.lower_bound_ = self.lower_bound_[0]
                self.upper_bound_ = self.upper_bound_[0]
            X[X < self.lower_bound_] = self.lower_bound_
            X[X > self.upper_bound_] = self.upper_bound_
        return X

    def get_feature_names_out(self, input_features=None):
        if input_features:
            if hasattr(self, 'feature_names_in_'):
                if len(self.feature_names_in_) != len(input_features):
                    raise ValueError(f"Length of input_features is {len(input_features)} while expected len(self.feature_names_in_)")
            return input_features
        else:
            if hasattr(self, 'feature_names_in_'):
                return self.feature_names_in_
            else:
                raise AttributeError("Has no attribute feature_names_in_, please use pd.DataFrame when training /testing")

##################################################################################################################
#       Named transformer
#
##################################################################################################################

def get_columns_from_columntransformer(column_transformer: ColumnTransformer, input_features) -> np.ndarray:
    n_in_transformers = len(column_transformer.transformers)
    n_out_transformers = len(
        column_transformer.transformers_)  # If there are remaining columns, then len(transformers_)==len(transformers)+1, otherwise len(transformers_)==len(transformers).

    # for passed in transformers (excluding remindars)
    col_name = []
    raw_names = []
    for name, fitted_transformer, raw_col_names in column_transformer.transformers_[
                                                   :n_in_transformers]:  # the last transformer could be ColumnTransformer's 'remainder'

        # Warning: for Columntransformer who uses callable column selector, there is possibility
        # that there were no columns selected for this thread, this will be the unfitted transformer,
        # and the corresponding raw_col_names will be empty [].
        # ref: https://github.bns/scikit-learn/scikit-learn/issues/19014
        if raw_col_names is None:
            raw_col_names = []
        else:
            raw_col_names = list(raw_col_names)

        if not raw_col_names:
            # if raw_col_names = [] or None, indicates its unused during training and should be dropped,
            # the transformer will also be unfitted
            logging.info(
                f"Column name getter(Column transformer): unused columns, will drop: ({name}, {fitted_transformer}, {raw_col_names})")
            continue

        # try to use original get_feature_names_out
        names = get_feature_names_out(fitted_transformer, raw_col_names)

        if isinstance(names, (np.ndarray, pd.Series, pd.Index)):  # eg.
            col_name += names.tolist()
        elif isinstance(names, list):
            col_name += names
        elif isinstance(names, str):
            col_name.append(names)

        raw_names.extend(raw_col_names)

    # find input feature names
    if input_features is None:
        input_features = raw_names

    # add remiander columns if any
    if n_out_transformers > n_in_transformers and column_transformer.remainder != 'drop':
        _, _, reminder_columns = column_transformer.transformers_[-1]

        for col_idx in reminder_columns:
            col_name.append(input_features[col_idx])

    return np.array(col_name)


def get_columns_from_imputer(imputer: Union[SimpleImputer, IterativeImputer, KNNImputer], input_features,
                             prefix: str = '_naFlag') -> np.ndarray:
    if input_features is None:
        input_features = imputer.feature_names_in_

    if imputer.add_indicator:
        missing_indicator_indices = imputer.indicator_.features_
        missing_indicators = [input_features[idx] + prefix for idx in missing_indicator_indices]
        transformed_colnames = list(input_features) + missing_indicators

    else:
        transformed_colnames = list(input_features)
    return np.array(transformed_colnames)


def get_feature_names_out(transformer, input_features):
    if isinstance(transformer, (SimpleImputer, IterativeImputer, KNNImputer)):
        transformed_colnames = get_columns_from_imputer(transformer, input_features)

    elif isinstance(transformer, ColumnTransformer):
        transformed_colnames = get_columns_from_columntransformer(transformer, input_features)

    elif isinstance(transformer, Pipeline):
        stepname, transformer = transformer.steps[-1]  # the last step in the pipeline
        transformed_colnames = get_feature_names_out(transformer, None)

    elif isinstance(transformer, SFS):
        # designed for mlxtend.SequentialFeatureSelector
        transformed_colnames = transformer.k_feature_names_

    else:
        if callable(getattr(transformer, "get_feature_names_out", None)):
            transformed_colnames = transformer.get_feature_names_out(input_features)
        elif callable(getattr(transformer, "get_feature_names", None)):
            # designed for transformers under categ_encoders
            transformed_colnames = transformer.get_feature_names()
        else:  # if no 'get_feature_names' function, use raw column name
            transformed_colnames = input_features

    return np.array(transformed_colnames)


class NamedTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, transformer):
        """Add column names to output
        support ColumnTransformer and Imputers (with additional indicator)

        :param transformer: the sklearn compatible transformer
        """
        self.transformer = transformer
        self.feature_names_in_ = None

    def get_feature_names_out(self, input_features=None):
        if input_features is None:
            input_features = self.feature_names_in_

        transformed_colnames = get_feature_names_out(self.transformer, input_features)

        return transformed_colnames

    def fit(self, X, y=None):
        self.transformer.fit(X, y)

        if hasattr(self.transformer, 'feature_names_in_'):
            self.feature_names_in_ = self.transformer.feature_names_in_
        elif isinstance(X, pd.DataFrame):
            self.feature_names_in_ = X.columns
        else:
            self.feature_names_in_ = None
        return self

    def transform(self, X, y=None):
        X_ = self.transformer.transform(X)
        columns = self.get_feature_names_out(self.feature_names_in_)
        return pd.DataFrame(X_, columns=columns)


def null_default(x, default):
    return default if x in [None, np.nan] else x


class TransformerHelper:
    def __init__(self, features: Union[list, np.ndarray, pd.Index] = None):
        self.features = np.asarray(features) if features is not None else np.asarray([])

    def build(self):
        raise NotImplementedError("")


class ImputeHelper(TransformerHelper):
    def __init__(self, features: Union[list, np.ndarray, pd.Index] = None, imputers: Union[tuple, list, dict] = None):
        """

        :param features: which features to apply encoder, if None, will apply to all features, then encs should be specified and in tuple/list, other wise use default values
        :param imputers: can be tuple, list,  dict or None
            # align with `OneHotEncoder`, see documentation for help
            if tuple or list, should be in format (strategy, const, indicator), will be applied to all features using same params
            if dict, should be format {'colname': (strategy, const, indicator)}, will be applied to specified features
            if None, will apply default imputation (mean imputation)
                -> strategy: can be 'mean', 'median', 'constant', 'most_frequent' or None/np.nan, default to 'mean'
                -> const: only effective when strategy = 'constant', will use for imputation, default to None
                -> indicator: True or False to specify whether to add a missing value indicator, default to False
        """
        super().__init__(features)
        self.imputers = imputers

    def build(self) -> Union[MyImputer, NamedTransformer]:
        if self.imputers is None:
            # if imputers is None, will apply default parameter, the `features` will specify which features to apply to
            return MyImputer(strategy='mean', fill_value=None, add_indicator=False)

        elif isinstance(self.imputers, (tuple, list)):
            strategy, const, indicator = self.imputers
            if not pd.isnull(const):
                strategy = 'constant'
            strategy = null_default(strategy, 'mean')
            indicator = null_default(indicator, False)
            return MyImputer(strategy=strategy, fill_value=const, add_indicator=indicator)

        elif isinstance(self.imputers, dict):
            # TODO: caution when self.features is set but are out of the keys of the imputers.keys()
            self.features = np.asarray(pd.Index(self.imputers.keys()).union(self.features, sort = False))
            imp_trans = []
            for colname, (strategy, const, indicator) in self.imputers.items():
                if not pd.isnull(const):
                    strategy = 'constant'
                strategy = null_default(strategy, 'mean')
                indicator = null_default(indicator, False)
                imp = MyImputer(strategy=strategy, fill_value=const, add_indicator=indicator)
                imp_trans.append((colname, imp, make_present_col_selector([colname])))
            return NamedTransformer(ColumnTransformer(imp_trans, remainder='passthrough', n_jobs=-1))


class OutlierClipperHelper(TransformerHelper):
    def __init__(self, features: Union[list, np.ndarray, pd.Index] = None, clippers: Union[tuple, list, dict] = None):
        """

        :param features: which features to apply encoder, if None, will apply to all features, then encs should be specified and in tuple/list, other wise use default values
        :param clippers: can be tuple, list, dict or None
            # align with `OutlierClipper`, see documentation for help
            if tuple or list, should be in format (strategy, quantile_range, constant_capper), will be applied to all numerical features using same strategy and params
            if dict, should be format {'colname': (strategy, quantile_range, constant_capper)}, will be applied to specified numerical features
            if None, will apply default OutlierClipper
                -> strategy: {'iqr' for IQR cut, 'quantile' for given quantile clip, 'constant' for constant value clip}, default to iqr
                -> quantile_range: a tuple of low and high quantile threshold, use when strategy = 'quantile', default to (5, 95)
                -> constant_capper: a tuple of constant low and high threshold, use when strategy = 'constant', default to None
        """
        super().__init__(features)
        self.clippers = clippers

    def build(self) -> Union[OutlierClipper, NamedTransformer]:
        if self.clippers is None:
            # if clippers is None, will apply default parameter, the `features` will specify which features to apply to
            return OutlierClipper(strategy='iqr', quantile_range=None, constant_capper=None)

        elif isinstance(self.clippers, (tuple, list)):
            strategy, quantile_range, constant_capper = self.clippers
            strategy = null_default(strategy, 'iqr')
            quantile_range = null_default(quantile_range, (5, 95))
            return OutlierClipper(strategy=strategy, quantile_range=quantile_range, constant_capper=constant_capper)

        elif isinstance(self.clippers, dict):
            # TODO: caution when self.features is set but are out of the keys of the clippers.keys()
            self.features = np.asarray(pd.Index(self.clippers.keys()).union(self.features, sort = False))
            outlier_trans = []
            for colname, (strategy, quantile_range, constant_capper) in self.clippers.items():
                strategy = null_default(strategy, 'iqr')
                quantile_range = null_default(quantile_range, (5, 95))
                oc = OutlierClipper(strategy=strategy, quantile_range=quantile_range, constant_capper=constant_capper)
                outlier_trans.append((colname, oc, make_present_col_selector([colname])))
            return NamedTransformer(ColumnTransformer(outlier_trans, remainder='passthrough', n_jobs=-1))


class ScalerHelper(TransformerHelper):
    def __init__(self, features: Union[list, np.ndarray, pd.Index] = None, scalers: Union[object, dict] = None):
        """

        :param features: which features to apply encoder, if None, will apply to all features, then encs should be specified and in tuple/list, other wise use default values
        :param scalers: can be object, dict or None
            # align with `sklearn Scalers`, see documentation for help
            if object, should be sklearn scalers or custom scaler transformers, will be applied to all features using same params
            if dict, should be format {'colname': scaler}, will be applied to specified features
            if None, will apply default scaling: StandardScaler
        """
        super().__init__(features)
        self.scalers = scalers

    def build(self) -> NamedTransformer:
        if self.scalers is None:
            # if imputers is None, will apply default parameter, the `features` will specify which features to apply to
            return NamedTransformer(StandardScaler())

        elif isinstance(self.scalers, dict):
            # TODO: caution when self.features is set but are out of the keys of the scalers.keys()
            self.features = np.asarray(pd.Index(self.scalers.keys()).union(self.features, sort = False))
            scaler_trans = []
            for colname, scaler in self.scalers.items():
                scaler = NamedTransformer(scaler)
                scaler_trans.append((colname, scaler, make_present_col_selector([colname])))
            return NamedTransformer(ColumnTransformer(scaler_trans, remainder='passthrough', n_jobs=-1))

        else:
            # just use the scaler provided
            return NamedTransformer(self.scalers)


class OnehotEncHelper(TransformerHelper):
    def __init__(self, features: Union[list, np.ndarray, pd.Index] = None, encs: Union[tuple, list, dict] = None):
        """

        :param features: which features to apply encoder, if None, will apply to all features, then encs should be specified and in tuple/list, other wise use default values
        :param encs: one hot encoder parameters, can be tuple, list,  dict or None
            # align with `OneHotEncoder`, see documentation for help
            if tuple or list, should be in format (categories, drop, handle_unknown), will be applied to all categorical features using same params
            if dict, should be format {'colname': (categories, drop, handle_unknown)}, will be applied to specified categorical features
            if None, will apply default one hot encoding
                -> categories: ‘auto’ : Determine categories automatically from the training data. or list: categories[i] holds the categories expected in the ith column
                -> drop: {‘first’, ‘if_binary’} default=None
                -> handle_unknown: {‘error’, ‘ignore’} default=’error’
        """
        super().__init__(features)
        self.encs = encs

    def build(self) -> NamedTransformer:
        if self.encs is None:
            # if encs is None, will apply default parameter, the `features` will specify which features to apply to
            return NamedTransformer(OneHotEncoder(categories='auto', handle_unknown='error', sparse=False, drop=None))

        elif isinstance(self.encs, (tuple, list)):
            categories, drop, handle_unknown = self.encs
            categories = null_default(categories, 'auto')
            handle_unknown = null_default(handle_unknown, 'ignore')
            return NamedTransformer(
                OneHotEncoder(categories=categories, handle_unknown=handle_unknown, sparse=False, drop=drop))

        elif isinstance(self.encs, dict):
            # TODO: caution when self.features is set but are out of the keys of the onehot_encs.keys()
            self.features = np.asarray(pd.Index(self.encs.keys()).union(self.features, sort = False))
            ohe_trans = []
            for colname, (categories, drop, handle_unknown) in self.encs.items():
                categories = null_default(categories, 'auto')
                handle_unknown = null_default(handle_unknown, 'ignore')
                ohe = NamedTransformer(
                    OneHotEncoder(categories=categories, handle_unknown=handle_unknown, sparse=False, drop=drop))
                ohe_trans.append((colname, ohe, make_present_col_selector([colname])))
            return NamedTransformer(ColumnTransformer(ohe_trans, remainder='passthrough', n_jobs=-1))


class OrdinalEncHelper(TransformerHelper):
    def __init__(self, features: Union[list, np.ndarray, pd.Index] = None, encs: Union[tuple, list, dict] = None):
        """

        :param features: which features to apply encoder, if None, will apply to all features if mapping is not set
        :param encs: ordinal encoder parameters, can be tuple, list,  dict or None
            # not align with `category_encoders.ordinal.OrdinalEncoder`, but similar, see documentation for help: https://contrib.scikit-learn.org/category_encoders/ordinal.html
            if tuple or list, should be in format (mapping, handle_unknown, handle_missing), and the features should be set!, otherwise will be no effect
            if dict, should be format {'colname': (mapping, handle_unknown, handle_missing)}, will be applied to specified categorical features
            if None, will apply default ordinal encoding
                -> mapping: dict of value mappings, e,g,  {None: 0, ‘a’: 1, ‘b’: 2, 'c' : 3}}, default to None  # Note this is a bit different from Ordinal Encoder!!!
                -> handle_unknown: ‘error’, ‘return_nan’ and ‘value’, defaults to ‘value’
                -> handle_missing: ‘error’, ‘return_nan’, and ‘value, default to ‘value’
        """
        super().__init__(features)
        self.encs = encs

    def build(self) -> Union[OrdinalEncoder, NamedTransformer]:
        if self.encs is None:
            # if encs is None, will apply default parameter, the `features` will specify which features to apply to
            return OrdinalEncoder(handle_unknown='value', handle_missing='value')

        elif isinstance(self.encs, (tuple, list)):
            mapping, handle_unknown, handle_missing = self.encs
            handle_unknown = null_default(handle_unknown, 'value')
            handle_missing = null_default(handle_missing, 'value')
            mappings = [{'col' : feat,  'mapping' : mapping} for feat in self.features]
            return OrdinalEncoder(mapping=mappings, handle_unknown=handle_unknown, handle_missing=handle_missing)

        elif isinstance(self.encs, dict):
            # TODO: caution when self.features is set but are out of the keys of the onehot_encs.keys()
            self.features = np.asarray(pd.Index(self.encs.keys()).union(self.features, sort = False))
            ode_trans = []
            for colname, (mapping, handle_unknown, handle_missing) in self.encs.items():
                handle_unknown = null_default(handle_unknown, 'value')
                handle_missing = null_default(handle_missing, 'value')
                mappings = [{'col': colname, 'mapping': mapping}]
                ode = OrdinalEncoder(mapping = mappings, handle_unknown = handle_unknown, handle_missing = handle_missing)
                ode_trans.append((colname, ode, make_present_col_selector([colname])))
            return NamedTransformer(ColumnTransformer(ode_trans, remainder = 'passthrough', n_jobs = -1))


class CountEncHelper(TransformerHelper):
    def __init__(self, features: Union[list, np.ndarray, pd.Index] = None, encs: Union[tuple, list, dict] = None):
        """

        :param features: which features to apply encoder, if None, will apply to all features, then encs should be specified and in tuple/list, other wise use default values
        :param encs: count encoder parameters, can be tuple, list,  dict or None
            # align with `category_encoders.count.CountEncoder`, see documentation for help: https://contrib.scikit-learn.org/category_encoders/count.html
            if tuple or list, should be in format (normalize, handle_unknown, handle_missing), will be applied to all categorical features using same params
            if dict, should be format {'colname': (normalize, handle_unknown, handle_missing)}, will be applied to specified categorical features
            if None, will apply default count encoding
                -> normalize: whether to normalize the counts to the range (0, 1), defaults to True
                -> handle_unknown: ‘error’, ‘return_nan’ and ‘value’, defaults to ‘value’,
                -> handle_missing: ‘error’, ‘return_nan’, and ‘value, default to ‘value’
        """
        super().__init__(features)
        self.encs = encs

    def build(self) -> Union[CountEncoder, NamedTransformer]:
        if self.encs is None:
            # if encs is None, will apply default parameter, the `features` will specify which features to apply to
            return CountEncoder(normalize=True, handle_unknown='value', handle_missing='value')

        elif isinstance(self.encs, (tuple, list)):
            normalize, handle_unknown, handle_missing = self.encs
            handle_unknown = null_default(handle_unknown, 'value')
            handle_missing = null_default(handle_missing, 'value')
            return CountEncoder(normalize=normalize, handle_unknown=handle_unknown, handle_missing=handle_missing)

        elif isinstance(self.encs, dict):
            # TODO: caution when self.features is set but are out of the keys of the onehot_encs.keys()
            self.features = np.asarray(pd.Index(self.encs.keys()).union(self.features, sort = False))
            coe_trans = []
            for colname, (normalize, handle_unknown, handle_missing) in self.encs.items():
                handle_unknown = null_default(handle_unknown, 'value')
                handle_missing = null_default(handle_missing, 'value')
                coe = CountEncoder(normalize=normalize, handle_unknown=handle_unknown, handle_missing=handle_missing)
                coe_trans.append((colname, coe, make_present_col_selector([colname])))
            return NamedTransformer(ColumnTransformer(coe_trans, remainder='passthrough', n_jobs=-1))


class SimplePreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self, pre_ignore = None, pre_drop = None, categorical_features=None,
                 imputers: ImputeHelper = None,
                 outlier_clippers: OutlierClipperHelper = None, log_features=None, scaler: ScalerHelper = None,
                 onehot_encs: OnehotEncHelper = None,
                 ordinal_encs: OrdinalEncHelper = None,
                 count_encs: CountEncHelper = None,
                 ):
        """A basic preprocessing pipeline tackling both numerical and categorical features

        :param pre_ignore: array of pre-excluded columns to ignore/passthrough
        :param pre_drop: array of pre-excluded columns to drop
        :param categorical_features: array-like of {bool, int, str} of shape (n_features) or shape (n_categorical_features,)
            if bool type, then use as boolean mask to identify categ features (True index)
            if int type, then use as index of categ features
            if str, then use as column name of categ features
            if None, by default will infer using pandas DataFrame's dtypes: 'object' or 'category'
        :param imputers: Impute helper object, if None, will skip this step
        :param outlier_clippers: outlier clipper helper object, if None, will skip this step
        :param log_features: array of str indicating which features need a log1p transformation
        :param scaler: scaler helper object, if None, will skip this step
        :param onehot_encs: one hot encoder helper object, if None, will skip this step
        :param ordinal_encs: ordinal encoder helper object, if None, will skip this step
        :param count_encs: count encoder helper object, if None, will skip this step

        """

        self.categorical_features = np.asarray(
            categorical_features) if categorical_features is not None else np.asarray([])
        self.imputers = imputers
        self.outlier_clippers = outlier_clippers
        self.log_features = np.asarray(log_features) if log_features is not None else np.asarray([])
        self.scaler = scaler
        self.onehot_encs = onehot_encs
        self.ordinal_encs = ordinal_encs
        self.count_encs = count_encs
        self.pre_ignore = pd.Index([]) if pre_ignore is None else pd.Index(pre_ignore)
        self.pre_drop = pd.Index([]) if pre_drop is None else pd.Index(pre_drop)

        self.feature_names_in_ = None

    def get_feature_names_out(self, input_features=None):
        if input_features is None:
            input_features = self.feature_names_in_

        transformed_colnames = get_feature_names_out(self.preprocess_pipe_, input_features)

        return transformed_colnames

    def fit(self, X, y=None):
        # type examination and remove pre-exclude columns
        if isinstance(X, pd.DataFrame):
            # remove pre_drop features from the dataset
            columns = X.columns.difference(self.pre_drop, sort = False)
            X = X[columns]
            # remove pre_ignore features from the column
            columns = X.columns.difference(self.pre_ignore, sort = False)
        else:
            raise TypeError("X can only be pandas dataframe")

        # numerical vs. categorical
        if self.categorical_features.size > 0:
            # for numpy arrays, a.dtype.kind: U - str, i - int, f - float, b - bool, O - object
            if self.categorical_features.dtype.kind in ('U', 'O'):
                categ_feats = pd.Index(self.categorical_features).intersection(columns)
                num_feats = columns.difference(categ_feats, sort=False)
            elif self.categorical_features.dtype.kind in ('b', 'i'):
                if len(self.categorical_features) != len(columns):
                    raise ValueError(
                        f"if categorical_features is bool array (categorical mask) or int array (categorical index), its length should match X.shape[1]")
                else:
                    categ_feats = columns[self.categorical_features]
                    num_feats = columns.difference(categ_feats, sort=False)
            else:
                raise TypeError(
                    f"categorical_features can only be in type int, bool and str array, got {self.categorical_features.dtype}")

        else:
            categ_feats = columns.intersection(X.select_dtypes(include=['object', 'category']).columns)
            num_feats = columns.intersection(X.select_dtypes(include=['number']).columns)

        preprocess_trans = []
        # 1 imputation for missing values
        if self.imputers:
            impute_pipe = self.imputers.build()
            preprocess_trans.append(('impute', impute_pipe))

        # 2 numerical features handling
        num_trans = []

        # 2.1 outlier clipper
        if self.outlier_clippers is not None:
            oc_pipe = self.outlier_clippers.build()
            # oc_features = self.outlier_clippers.features
            # if oc_features.size == 0:
            #    oc_features = num_feats.copy()
            num_trans.append(('clipper', oc_pipe))

        # 2.2 log transformation
        if self.log_features.size > 0:
            log_cols = pd.Index(self.log_features).intersection(columns)
            log_trans = [('log',
                          FunctionTransformer(func=np.log1p, inverse_func=np.expm1, validate=True, accept_sparse=True),
                          make_present_col_selector(log_cols))]
            log_pipe = NamedTransformer(ColumnTransformer(log_trans, remainder='passthrough', n_jobs=-1))
            num_trans.append(('log', log_pipe))

        # 2.3 scaler normalization
        if self.scaler:
            scaler_pipe = self.scaler.build()
            # scaler_features = self.scaler.features
            # if scaler_features.size == 0:
            #    scaler_features = num_feats.copy()
            num_trans.append(('scaler', scaler_pipe))

        # 3 categorical feature handling
        categ_trans = []

        # 3.2 categorical encoding handling (onehot, ordinal, count)
        categ_enc_trans = []  # to be a columnTransformer
        # 3.2.1 one hot encoding
        if self.onehot_encs is not None:
            ohe_pipe = self.onehot_encs.build()
            ohe_features = self.onehot_encs.features
            if ohe_features.size == 0:
                ohe_features = categ_feats.copy()
            categ_enc_trans.append(('ohe', ohe_pipe, make_present_col_selector(ohe_features)))

        # 3.2.2 ordinal encoding
        if self.ordinal_encs is not None:
            ode_pipe = self.ordinal_encs.build()
            ode_features = self.ordinal_encs.features
            if ode_features.size == 0:
                ode_features = categ_feats.copy()
            categ_enc_trans.append(('ode', ode_pipe, make_present_col_selector(ode_features)))

        # 3.2.3 count encoders
        if self.count_encs is not None:
            coe_pipe = self.count_encs.build()
            coe_features = self.count_encs.features
            if coe_features.size == 0:
                coe_features = categ_feats.copy()
            categ_enc_trans.append(('coe', coe_pipe, make_present_col_selector(coe_features)))

        # TODO: add count encoder, add BucketValuer, pipeline(bucketvalue, columntransformer(ohe, ode, coe)), n_jobs = -1
        if categ_enc_trans:
            categ_enc_pipe = NamedTransformer(ColumnTransformer(categ_enc_trans, remainder='passthrough', n_jobs=-1))
            categ_trans.append(('enc', categ_enc_pipe))

        # assemble pipeline
        # combine category and numerical
        num_categ_trans = []
        if num_trans:
            num_categ_trans.append(('num', Pipeline(num_trans), make_present_col_selector(num_feats)))
        if categ_trans:
            num_categ_trans.append(('categ', Pipeline(categ_trans), make_present_col_selector(categ_feats)))

        if num_categ_trans:
            num_categ_pipe = NamedTransformer(ColumnTransformer(num_categ_trans, remainder='passthrough', n_jobs=-1))
            preprocess_trans.append(('num_categ', num_categ_pipe))

        self.preprocess_pipe_ = NamedTransformer(Pipeline(preprocess_trans))
        self.preprocess_pipe_.fit(X, y)

        return self

    def transform(self, X, y=None):
        return self.preprocess_pipe_.transform(X, y)

##################################################################################################################
#       Feature Selection
#
##################################################################################################################

class PreliminaryFeatureSelector:

    def __init__(self, X: pd.DataFrame, y: Union[pd.DataFrame, pd.Series], featureMeta: FeatureMeta,  problem_type: str = 'classif'):
        """

        :param X: X in pandas DataFrame type
        :param y: target of the algorithm
        :param featureMeta: the featureMeta helper class to load table schema
        :param problem_type: 'classif' for classification problem and 'regress' for regression problem
        """
        self.X = X
        self.y = y
        self.featureMeta = featureMeta
        self.init_cols = X.columns
        self.problem_type = check_params(problem_type, allowed_values=['classif', 'regress'])
        self.reset()

    def reset(self):
        self.filtered_cols = self.init_cols.copy()
        # add the logger to record the steps
        self.logger = pd.DataFrame(columns = ['Step', 'Pre#', 'Post#', 'Drop#', 'Drop%', 'Metric', 'Threshold', 'RemovedCols'])

    def stepback(self) -> pd.Series:
        """one step backward

        :return: a series of colnames and values as 0 just for structural considerations
        """
        pre_len = len(self.filtered_cols)

        last_dropped = self.logger['RemovedCols'].iloc[-1]
        self.filtered_cols = self.filtered_cols.union(last_dropped)

        post_len = len(self.filtered_cols)
        print(f"Step back: {post_len - pre_len} features added (from {pre_len} to {post_len})")
        print(f"Added back features: {last_dropped.tolist()}")

        self.logger = self.logger.iloc[:-1,:]
        return pd.Series(last_dropped, np.ones(len(last_dropped)))


    def get_report(self, summarize:bool = False) -> pd.DataFrame:
        """return a pandas dataframe report

        :param summarize: if True, will report overall report, otherwise will report details by step
        :return:
        """
        if summarize:
            summ = {
                'Pre#' : self.logger['Pre#'].iloc[0],
                'Post#': self.logger['Post#'].iloc[-1],
                'Drop#': self.logger['Drop#'].sum(),
                'Drop%': self.logger['Drop#'].sum() / self.logger['Pre#'].iloc[0],
                'RemovedCols': np.array(self.logger['RemovedCols'].apply(lambda x: list(x)).sum())
            }
            return pd.DataFrame.from_records([summ])
        else:
            return self.logger

    def filter_id_policy(self, add_id_policy_cols: list = None) -> pd.Series:
        """filter out features that violates policy restriction or such fields as Ids that should not be modeled

        :param add_id_policy_cols: additional list of id_policy type features that are not captured in featureMeta
        :return: a series of colnames and values as 0 just for structural considerations
        """
        pre_len = len(self.filtered_cols)
        id_policy_cols = self.featureMeta.getIdPolicyFeatures().tolist()
        if add_id_policy_cols:
            id_policy_cols.extend(add_id_policy_cols)

        self.filtered_cols = self.filtered_cols.difference(id_policy_cols)
        post_len = len(self.filtered_cols)
        print(f"id_policy filter: {pre_len - post_len} features eliminated (from {pre_len} to {post_len})")
        print(f"Reduced features: {id_policy_cols}")

        self.logger = self.logger.append({
            'Step' : 'IdPolicy' , 'Pre#' : pre_len, 'Post#' : post_len,
            'Drop#' : pre_len - post_len, 'Drop%' : (pre_len - post_len) / pre_len,
            'Metric' : np.nan, 'Threshold' : np.nan, 'RemovedCols' : np.array(id_policy_cols)
        } , ignore_index = True)

        return pd.Series(id_policy_cols, np.ones(len(id_policy_cols)))


    def filter_missing_rate(self, threshold: float = 0.25) -> pd.Series:
        """filter out features whose missing rate is higher than the threshold

        :param threshold: a number between 0 and 1
        :return: each feature's missing rate
        """
        subset = self.X[self.filtered_cols]
        n, pre_len = subset.shape
        missings = subset.isna().sum() / n
        dropped_cols = missings[missings >= threshold].index
        self.filtered_cols = missings[missings < threshold].index
        post_len = len(self.filtered_cols)
        print(
            f"missing rate filter (threshold = {threshold}): {pre_len - post_len} features eliminated (from {pre_len} to {post_len})")
        print(f"Reduced features: {dropped_cols.tolist()}")

        self.logger = self.logger.append({
            'Step' : 'Missing Values' , 'Pre#' : pre_len, 'Post#' : post_len,
            'Drop#' : pre_len - post_len, 'Drop%' : (pre_len - post_len) / pre_len,
            'Metric' : 'Missing Rate', 'Threshold' : threshold,
            'RemovedCols' : np.array(dropped_cols)
        } , ignore_index = True)

        return missings.sort_values(ascending = False)  # return the result

    def filter_variance(self, threshold_num: float = 0.01, threshold_categ: float = 0) -> pd.Series:
        """Remove features whose variance is lower than the threshold (work for both numerical and categorical features)
        will filter numerical and categorical features separately
        for numerical features, will first normalize and then calculate the variance
        for categorical features, will first ordinal encode and then calculate the varaince

        :param threshold_num: the variance threshold to apply for numerical features (normalized)
        :param threshold_categ: the variance threshold to apply for categorical features (ordinal encoded)
        :return: each feature with its variance, first numerical then categorical
        """
        pre_len = len(self.filtered_cols)
        num_features = self.filtered_cols.intersection(self.featureMeta.getNumericFeatures())
        categ_features = self.filtered_cols.intersection(self.featureMeta.getCategFeatures())

        # numerical variance threshold
        num_pipe = Pipeline([
            ('scale', NamedTransformer(RobustScaler())),
            ('variance', VarianceThreshold(threshold=threshold_num))
        ])
        num_pipe.fit(self.X[num_features])
        num_var = num_pipe['variance']
        dropped_cols_num = num_features.difference(num_var.feature_names_in_[num_var.get_support()])

        # categorical variance threshold
        categ_pipe = Pipeline([
            ('ode', OrdinalEncoder()),
            ('variance', VarianceThreshold(threshold=threshold_categ))
        ])
        categ_pipe.fit(self.X[categ_features])
        categ_var = categ_pipe['variance']
        dropped_cols_categ = categ_features.difference(categ_var.feature_names_in_[categ_var.get_support()])

        dropped_cols = dropped_cols_num.union(dropped_cols_categ, sort=False)

        self.filtered_cols = self.filtered_cols.difference(dropped_cols_num, sort=False)
        dropped_num_len = pre_len - len(self.filtered_cols)
        self.filtered_cols = self.filtered_cols.difference(dropped_cols_categ, sort=False)
        dropped_categ_len = pre_len - len(self.filtered_cols) - dropped_num_len
        post_len = len(self.filtered_cols)
        print(
            f"Variance Threshold filter (threshold = Num: {threshold_num} | Categ: {threshold_categ}): {pre_len - post_len} features eliminated (from {pre_len} to {post_len}), (Num {dropped_num_len} + Categ {dropped_categ_len})")
        print(f"Reduced features: {dropped_cols.tolist()}")

        self.logger = self.logger.append({
            'Step': 'Variance Threshold', 'Pre#': pre_len, 'Post#': post_len,
            'Drop#': pre_len - post_len, 'Drop%': (pre_len - post_len) / pre_len,
            'Metric': 'Variance', 'Threshold': (threshold_num, threshold_categ),
            'RemovedCols': np.array(dropped_cols)
        }, ignore_index=True)

        v_num = pd.Series(data=num_var.variances_, index=num_var.feature_names_in_).sort_values(ascending=False)
        v_categ = pd.Series(data=categ_var.variances_, index=categ_var.feature_names_in_).sort_values(ascending=False)
        return pd.concat([v_num, v_categ])

    def filter_univariate(self, drop_ratio: float = 0.5) -> pd.Series:
        """Remove features whose score(mutual information by default) is in the lowest percentile
        will apply imputation and ordinal encoder for categorical variable

        :param drop_ratio: ratio between 0 and 1
        :return: scores of each variable (default using mutual information score)
        """
        pre_len = len(self.filtered_cols)

        num_features = self.filtered_cols.intersection(self.featureMeta.getNumericFeatures())
        categ_features = self.filtered_cols.intersection(self.featureMeta.getCategFeatures())
        orderedCateg_features = self.filtered_cols.intersection(self.featureMeta.getFeaturesByTypes(['OrderedCateg']))
        unorderedCateg_features = self.filtered_cols.intersection(
            self.featureMeta.getFeaturesByTypes(['UnorderedCateg']))
        binary_features = self.filtered_cols.intersection(self.featureMeta.getFeaturesByTypes(['Binary']))

        # impute missing values before sending to scoring function
        features = num_features.union(categ_features)

        # compiling preprocessing unit
        imputers = {}
        for col in features:
            strategy, const = self.featureMeta.getImputeStrategyAndConst(col)
            imputers[col] = (strategy, const, False)
        imph = ImputeHelper(imputers=imputers)

        odeh = OrdinalEncHelper()

        preprocess = SimplePreprocessor(
            pre_ignore=None,
            categorical_features=categ_features,
            imputers=imph,
            outlier_clippers=None,
            log_features=None,
            scaler=None,
            onehot_encs=None,
            ordinal_encs=odeh
        )

        X_preprocessed = preprocess.fit_transform(self.X[self.filtered_cols])

        feature_names = pd.Index(preprocess.get_feature_names_out())
        categ_feature_bools = feature_names.isin(categ_features)

        # scoring function pipeline
        if self.problem_type == 'classif':
            score_func = partial(mutual_info_classif, discrete_features=categ_feature_bools)
        elif self.problem_type == 'regress':
            score_func = partial(mutual_info_regression, discrete_features=categ_feature_bools)
        else:
            raise ValueError("problem_type must be either classif or regress")

        keep_percent = 100 - 100 * drop_ratio
        scorer = SelectPercentile(score_func, percentile=keep_percent)
        scorer.fit(X_preprocessed, self.y)

        scores = pd.Series(data=scorer.scores_, index=scorer.feature_names_in_)
        threshold = scores[scorer.get_feature_names_out()].min()

        dropped_cols = self.filtered_cols.difference(feature_names[scorer.get_support()])

        self.filtered_cols = self.filtered_cols.difference(dropped_cols)
        post_len = len(self.filtered_cols)
        print(
            f"Univariate (mutual information score) filter (drop percent = {100 * drop_ratio}%, threshold = {threshold}): {pre_len - post_len} features eliminated (from {pre_len} to {post_len})")
        print(f"Reduced features: {dropped_cols.tolist()}")

        self.logger = self.logger.append({
            'Step': 'Univaraite Correlation', 'Pre#': pre_len, 'Post#': post_len,
            'Drop#': pre_len - post_len, 'Drop%': (pre_len - post_len) / pre_len,
            'Metric': 'Mutual Info', 'Threshold': threshold,
            'RemovedCols': np.array(dropped_cols)
        }, ignore_index=True)

        return scores.sort_values(ascending=False)

    def filter_importance(self, threshold: Union[float, str] = "0.6*median", scorer=None) -> pd.Series:
        """Remove features whose feature importance(gradient boosting tree by default) is in the lowest percentile
        will apply imputation and frequency encoder for categorical variable and robust scaler for numerical variable

        :param threshold: The threshold value to use for feature selection.
                Features whose importance is greater or equal are kept while the others are discarded.
                If “median” (resp. “mean”), then the threshold value is the median (resp. the mean) of the feature importances.
                A scaling factor (e.g., “1.25*mean”) may also be used.
                If None and if the estimator has a parameter penalty set to l1, either explicitly or implicitly (e.g, Lasso),
                the threshold used is 1e-5.
        :param scorer: The base estimator from which the transformer is built.
                This can be both a fitted (if prefit is set to True) or a non-fitted estimator.
                The estimator should have a feature_importances_ or coef_ attribute after fitting.
                Otherwise, the importance_getter parameter should be used.
        :return: feature importance/coeff of each variable (default using gradient boosting tree)
        """
        pre_len = len(self.filtered_cols)

        num_features = self.filtered_cols.intersection(self.featureMeta.getNumericFeatures())
        categ_features = self.filtered_cols.intersection(self.featureMeta.getCategFeatures())

        # impute missing values before sending to scoring function
        features = num_features.union(categ_features)

        # compiling preprocessing unit
        imputers = {}
        for col in features:
            strategy, const = self.featureMeta.getImputeStrategyAndConst(col)
            imputers[col] = (strategy, const, False)
        imph = ImputeHelper(imputers=imputers)
        # add robust scaler for numerical features
        sch = ScalerHelper(scalers=RobustScaler())
        # add count encoder (frequency encoder) for categorical features
        ceh = CountEncHelper(encs=(True, 'value', 'value'))

        preprocess = SimplePreprocessor(
            pre_ignore=None,
            categorical_features=categ_features,
            imputers=imph,
            outlier_clippers=None,
            log_features=None,
            scaler=sch,
            onehot_encs=None,
            ordinal_encs=None,
            count_encs=ceh
        )
        X_preprocessed = preprocess.fit_transform(self.X[self.filtered_cols])
        feature_names = pd.Index(preprocess.get_feature_names_out())

        # use model's feature_importance_ or coeff_ to select
        if scorer is None:
            if self.problem_type == 'classif':
                scorer = BalancedRandomForestClassifier(n_estimators=100)
            elif self.problem_type == 'regress':
                scorer = RandomForestRegressor(n_estimators=100)
            else:
                raise ValueError("problem_type must be either classif or regress")

        selector = SelectFromModel(estimator=scorer, threshold=threshold)
        selector.fit(X_preprocessed, self.y)

        dropped_cols = self.filtered_cols.difference(feature_names[selector.get_support()])

        self.filtered_cols = self.filtered_cols.difference(dropped_cols)
        post_len = len(self.filtered_cols)
        print(
            f"Model selection (feature importance or coeff score) filter (threshold = {selector.threshold_}): {pre_len - post_len} features eliminated (from {pre_len} to {post_len})")
        print(f"Reduced features: {dropped_cols.tolist()}")

        if hasattr(selector.estimator_, "coef_"):
            scores = selector.estimator_.coef_
            metric = 'Coefficient'
        elif hasattr(selector.estimator_, "feature_importances_"):
            scores = selector.estimator_.feature_importances_
            metric = 'Feature Importance'
        else:
            raise ValueError("Can only pass in model who has either coef_ or feature_importances_")

        self.logger = self.logger.append({
            'Step': 'Model Scoring', 'Pre#': pre_len, 'Post#': post_len,
            'Drop#': pre_len - post_len, 'Drop%': (pre_len - post_len) / pre_len,
            'Metric': metric, 'Threshold': selector.threshold_,
            'RemovedCols': np.array(dropped_cols)
        }, ignore_index=True)

        return pd.Series(data=scores, index=selector.feature_names_in_).sort_values(ascending=False)

    def filter_sequential(self, direction: str = 'backward', drop_ratio: float = 0.4, soft_drop_ratio: float = None,
                          scoring=None, scorer=None, cv=5) -> pd.DataFrame:
        """Use forward selection / backward elimination process for feature selection, based on the CV score of the specified model

        :param direction: {‘forward’, ‘backward’}, default=’forward’
        :param drop_ratio: ratio between 0 and 1, to drop how many features
        :param soft_drop_ratio: max/min features to drop(backward)/add(forward), if specified, will not use 'drop ratio' anymore, but find the optimal subset of features based on the CV scores
        :param scoring: str, callable, list/tuple or dict, default=None (use roc_auc for classification and neg_mean_squared_error for regression)
                If str, uses a sklearn scoring metric string identifier, for example {accuracy, f1, precision, recall, roc_auc} for classifiers,
                 {'mean_absolute_error', 'mean_squared_error'/'neg_mean_squared_error', 'median_absolute_error', 'r2'} for regressors.
                If a callable object or function is provided, it has to be conform with sklearn's signature scorer(estimator, X, y)
                http://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html
        :param scorer: scikit-learn classifier or regressor, by default will use BalancedRandomForestClassifier for classification and RandomForestRegressor for regression
        :param cv:int (default: 5) Integer or iterable yielding train, test splits.
                If cv is an integer and estimator is a classifier (or y consists of integer class labels) stratified k-fold.
                Otherwise regular k-fold cross-validation is performed. No cross-validation if cv is None, False, or 0.
        :return: a pandas DataFrame containing CV key results: ['feature_names', 'avg_score', 'std_dev', 'std_err', 'ci_bound', 'safe_score']
                ci_bound = N(0.95) * std_err
                safe_score = avg_score - ci_bound  # the lower confidence interval boundary for a safe and conservative estimation
        """

        optim_flag = (soft_drop_ratio is not None)

        pre_len = len(self.filtered_cols)

        num_features = self.filtered_cols.intersection(self.featureMeta.getNumericFeatures())
        categ_features = self.filtered_cols.intersection(self.featureMeta.getCategFeatures())

        # impute missing values before sending to scoring function
        features = num_features.union(categ_features)

        # compiling preprocessing unit
        imputers = {}
        for col in features:
            strategy, const = self.featureMeta.getImputeStrategyAndConst(col)
            imputers[col] = (strategy, const, False)
        imph = ImputeHelper(imputers=imputers)
        # add robust scaler for numerical features
        sch = ScalerHelper(scalers=RobustScaler())
        # add count encoder (frequency encoder) for categorical features
        ceh = CountEncHelper(encs=(True, 'value', 'value'))

        preprocess = SimplePreprocessor(
            pre_ignore=None,
            categorical_features=categ_features,
            imputers=imph,
            outlier_clippers=None,
            log_features=None,
            scaler=sch,
            onehot_encs=None,
            ordinal_encs=None,
            count_encs=ceh
        )
        X_preprocessed = preprocess.fit_transform(self.X[self.filtered_cols])
        feature_names = pd.Index(preprocess.get_feature_names_out())

        # use metric score or model's scoring method to select
        if scorer is None:
            if self.problem_type == 'classif':
                scorer = BalancedRandomForestClassifier(n_estimators=100)
            elif self.problem_type == 'regress':
                scorer = RandomForestRegressor(n_estimators=100)
            else:
                raise ValueError("problem_type must be either classif or regress")

        # scikit-learn approach, drawback: no scores output
        # selector = SequentialFeatureSelector(estimator = scorer, n_features_to_select = 1 - drop_ratio, direction = direction, scoring = scoring, cv = cv, n_jobs = -1)
        # mlxtend approach, can output score
        forward_bool = True if direction == 'forward' else False
        # if soft_drop_ratio is specified, will train on this ratio, but only select the best performing feature set
        if optim_flag:
            k_features = int((1 - soft_drop_ratio) * X_preprocessed.shape[1])
        else:
            k_features = int((1 - drop_ratio) * X_preprocessed.shape[1])

        if scoring is None:
            scoring = 'roc_auc' if self.problem_type == 'classif' else 'neg_mean_squared_error'

        selector = SFS(estimator=scorer, k_features=k_features, forward=forward_bool, verbose=2, scoring=scoring, cv=cv,
                       n_jobs=-1)
        selector.fit(X_preprocessed, self.y)

        alpha = 0.95
        cv_results_ = pd.DataFrame.from_dict(selector.get_metric_dict(confidence_interval=alpha)).T
        cv_results_[['avg_score', 'std_dev', 'ci_bound', 'std_err']] = cv_results_[
            ['avg_score', 'std_dev', 'ci_bound', 'std_err']].astype('float32')
        cv_results_['safe_score'] = cv_results_['avg_score'] - cv_results_['ci_bound'].fillna(
            0)  # lower bound of the 95% CI of the score, like Value at Risk, safe and conservative

        if optim_flag:
            idx_optim = cv_results_['safe_score'].argmax()
            retained_cols = cv_results_.iloc[idx_optim]['feature_names']
            dropped_cols = self.filtered_cols.difference(retained_cols)
            self.filtered_cols = pd.Index(retained_cols)
            threshold = cv_results_.iloc[idx_optim]['safe_score']
        else:
            dropped_cols = self.filtered_cols.difference(selector.k_feature_names_)
            self.filtered_cols = pd.Index(selector.k_feature_names_)
            threshold = selector.k_score_

        post_len = len(self.filtered_cols)
        print(
            f"Sequential Feature Selection ({direction}) filter: {pre_len - post_len} features eliminated (from {pre_len} to {post_len})")
        print(f"Reduced features: {dropped_cols.tolist()}")

        self.logger = self.logger.append({
            'Step': 'Sequential Feature Selection', 'Pre#': pre_len, 'Post#': post_len,
            'Drop#': pre_len - post_len, 'Drop%': (pre_len - post_len) / pre_len,
            'Metric': scoring, 'Threshold': threshold,
            'RemovedCols': np.array(dropped_cols)
        }, ignore_index=True)

        return cv_results_[['feature_names', 'avg_score', 'std_dev', 'std_err', 'ci_bound', 'safe_score']]

class FeaturePrescreen(SelectorMixin, BaseEstimator):
    def __init__(self,
            feature_meta: FeatureMeta,
            problem_type: str = 'classif',
            add_id_policy_cols: list = None,
            threshold_missing: float = 0.25,
            threshold_variance_num: float = 0.01,
            threshold_variance_categ: float = 0,
            threshold_importance: Union[float, str] = "0.6*median",
            scorer_importance = None,
            drop_ratio_score: float = 0.5,
            direction_seq: str = 'backward',
            drop_ratio_seq: float = 0.4,
            soft_drop_ratio_seq: float = None,
            scoring_seq = None,
            scorer_seq = None,
            cv_seq = 5,
            exec_sequence: str = "pmvui"
        ):
        """A preliminary feature selector

        :param featureMeta: the featureMeta helper class to load table schema
        :param problem_type: 'classif' for classification problem and 'regress' for regression problem

        -- Id Policy elimination parameters
        :param add_id_policy_cols: additional list of id_policy type features that are not captured in featureMeta

        -- Missing rate elimination parameters
        :param threshold_missing: a number between 0 and 1, maximum missing rate for retain the feature

        -- Variance Threshold elimination parameters
        :param threshold_variance_num: the variance threshold to apply for numerical features (normalized)
        :param threshold_variance_categ: the variance threshold to apply for categorical features (ordinal encoded)

        -- Feature importance filter parameters
        :param threshold_importance:The threshold value to use for feature selection.
                Features whose importance is greater or equal are kept while the others are discarded.
                If “median” (resp. “mean”), then the threshold value is the median (resp. the mean) of the feature importances.
                A scaling factor (e.g., “1.25*mean”) may also be used.
                If None and if the estimator has a parameter penalty set to l1, either explicitly or implicitly (e.g, Lasso),
                the threshold used is 1e-5.
        :param scorer_importance:The base estimator from which the transformer is built.
                This can be both a fitted (if prefit is set to True) or a non-fitted estimator.
                The estimator should have a feature_importances_ or coef_ attribute after fitting.
                Otherwise, the importance_getter parameter should be used.

        -- univariate feature selection parameters
        :param drop_ratio_score: ratio between 0 and 1, the percentage of features to drop

        -- Sequential Feature Selection Parameters
        :param direction_seq: {‘forward’, ‘backward’}, default=’forward’
        :param drop_ratio_seq: ratio between 0 and 1, to drop how many features
        :param soft_drop_ratio_seq: max/min features to drop(backward)/add(forward), if specified, will not use 'drop ratio' anymore, but find the optimal subset of features based on the CV scores
        :param scoring_seq: str, callable, list/tuple or dict, default=None (use roc_auc for classification and neg_mean_squared_error for regression)
                If str, uses a sklearn scoring metric string identifier, for example {accuracy, f1, precision, recall, roc_auc} for classifiers,
                 {'mean_absolute_error', 'mean_squared_error'/'neg_mean_squared_error', 'median_absolute_error', 'r2'} for regressors.
                If a callable object or function is provided, it has to be conform with sklearn's signature scorer(estimator, X, y)
                http://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html
        :param scorer_seq: scikit-learn classifier or regressor, by default will use BalancedRandomForestClassifier for classification and RandomForestRegressor for regression
        :param cv_seq:int (default: 5) Integer or iterable yielding train, test splits.
                If cv is an integer and estimator is a classifier (or y consists of integer class labels) stratified k-fold.
                Otherwise regular k-fold cross-validation is performed. No cross-validation if cv is None, False, or 0.
        :param exec_sequence: a string recording the sequence of steps included:
                p -- filter_id_policy (drop features that are Ids, or violates policy restrictions
                m -- filter_missing_rate (missing rate drop)
                v -- filter_variance (variance threshold)
                u -- filter_univariate (mutual infomation score)
                i -- filter_importance (feature importance)
                s -- sequential feature selection (forward/backward)
                B -- step back (remove previous step)

                e.g.,  you can pass in 'pmvuiuiui' for several rounds of feature importance/univariate filter
        """
        self.feature_meta = feature_meta
        self.pfs = None
        self.problem_type = problem_type
        self.add_id_policy_cols = add_id_policy_cols
        self.threshold_missing = threshold_missing
        self.threshold_variance_num = threshold_variance_num
        self.threshold_variance_categ = threshold_variance_categ
        self.threshold_importance = threshold_importance
        self.scorer_importance = scorer_importance
        self.drop_ratio_score = drop_ratio_score
        self.direction_seq = direction_seq
        self.drop_ratio_seq = drop_ratio_seq
        self.soft_drop_ratio_seq = soft_drop_ratio_seq
        self.scoring_seq = scoring_seq
        self.scorer_seq = scorer_seq
        self.cv_seq = cv_seq
        self.exec_sequence = exec_sequence

        self.metrics_history_ = {
            'p': [],
            'm': [],
            'v': [],
            'u': [],
            'i': [],
            's': [],
            'B': []
        }

    def _more_tags(self):
        return {"requires_y": True}

    def fit(self, X, y = None):
        # if X does not have column, try to add it using x0,x1,x2,....etc.
        if isinstance(X, np.ndarray):
            columns = [f'x{i}' for i in range(X.shape[1])]
            X = pd.DataFrame(X, columns = columns)

        self.feature_names_in_ = np.array(X.columns)
        self.pfs_ = PreliminaryFeatureSelector(X = X, y = y, featureMeta = self.feature_meta, problem_type = self.problem_type)

        # define the steps
        mapps = {
            'p' : partial(self.pfs_.filter_id_policy, add_id_policy_cols = self.add_id_policy_cols),
            'm' : partial(self.pfs_.filter_missing_rate, threshold = self.threshold_missing),
            'v' : partial(self.pfs_.filter_variance, threshold_num = self.threshold_variance_num, threshold_categ = self.threshold_variance_categ),
            'u' : partial(self.pfs_.filter_univariate, drop_ratio = self.drop_ratio_score),
            'i' : partial(self.pfs_.filter_importance, threshold = self.threshold_importance, scorer = self.scorer_importance),
            's' : partial(self.pfs_.filter_sequential, direction = self.direction_seq, drop_ratio = self.drop_ratio_seq,
                          soft_drop_ratio = self.soft_drop_ratio_seq, scoring = self.scoring_seq, scorer = self.scorer_seq, cv = self.cv_seq),
            'B' : self.pfs_.stepback
        }

        for s in self.exec_sequence:
            if s in mapps.keys():
                step = mapps.get(s)
                metric = step()  # execute the step

                self.metrics_history_[s].append(metric)

        return self

    @ property
    def selector_(self):
        check_is_fitted(self)

        return self.pfs_

    def transform(self, X, y = None):
        if isinstance(X, np.ndarray):
            columns = [f'x{i}' for i in range(X.shape[1])]
            if len(columns) != len(self.feature_names_in_):
                raise ValueError(f"Suggest X being pandas DataFrame, shape mismatch, expected columns {len(self.feature_names_in_)} got {len(columns)}")
            X = pd.DataFrame(X, columns = columns)

        return X[self.get_feature_names_out()]

    def get_report(self, summarize:bool = False) -> pd.DataFrame:
        return self.selector_.get_report(summarize)

    def get_feature_names_out(self, input_features = None) -> np.ndarray:
        """Mask feature names according to selected features.

        :param input_features: If input_features is None, then feature_names_in_ is used as feature names in.
                If feature_names_in_ is not defined, then names are generated: [x0, x1, ..., x(n_features_in_)].
                If input_features is an array-like, then input_features must match feature_names_in_ if feature_names_in_ is defined.
        :return:
        """
        return np.array(self.selector_.filtered_cols)

    def _get_support_mask(self):
        check_is_fitted(self)

        mask = np.isin(self.feature_names_in_, self.get_feature_names_out())
        return mask

    def inverse_transform(self, X):
        """Reverse the transformation operation.

        :param X: input X
        :return: X with columns of zeros inserted where features would have been removed by transform.
        """
        X_ = pd.DataFrame(columns = self.feature_names_in_)

        if isinstance(X, np.ndarray):
            if X.shape[1] != len(self.get_feature_names_out()):
                raise ValueError(f"Suggest X being pandas DataFrame, shape mismatch, expected columns {len(self.get_feature_names_out())} got {X.shape[1]}")
            X_.loc[:, self.get_feature_names_out()] = X
        else:
            exist_cols = pd.Index(self.get_feature_names_out()).intersection(X.columns)
            X_.loc[:, exist_cols] = X.loc[:, exist_cols]

        return X_

