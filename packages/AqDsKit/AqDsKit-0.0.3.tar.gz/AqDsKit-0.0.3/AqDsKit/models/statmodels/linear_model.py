import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.regression

# https://www.statsmodels.org/stable/regression.html#
# https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.html#statsmodels.regression.linear_model.RegressionResults
# https://stats.stackexchange.com/questions/16493/difference-between-confidence-intervals-and-prediction-intervals
# https://stats.stackexchange.com/questions/136157/general-mathematics-for-confidence-interval-in-multiple-linear-regression


class LinearRegressionModeler:
    def __init__(self, regressors : list = None, y_label : str = None, formula : str = None):
        if formula:
            self.formula = formula
            self.regressors = None
            self.y_label = None
        else:
            self.formula = None
            self.regressors = regressors
            self.y_label = y_label

    def fit(self, train_df : pd.DataFrame):
        if self.formula:
            self.model = smf.ols(formula = self.formula, data = train_df)
        else:
            X = train_df[self.regressors]
            Y = train_df[self.y_label]
            self.model = sm.OLS(Y, sm.add_constant(X))

        self.results = self.model.fit()

    def getResults(self) -> statsmodels.regression.linear_model.RegressionResults:
        return self.results

    def getSummary(self):
        return self.results.summary()

    def t_inv(self, alpha = 0.05):
        return stats.t.ppf(1 - alpha / 2, self.results.df_resid)

    def predict(self, test_df : pd.DataFrame):
        if self.formula:
            return self.results.predict(test_df)
        else:
            X = test_df[self.regressors]
            # has_constant: https://stackoverflow.com/questions/36532529/add-constant-in-statsmodels-not-working
            return self.results.predict(sm.add_constant(X, has_constant = 'add'))

    def predict_detail(self, test_df : pd.DataFrame, alpha : float = 0.05):
        """
        Args:
            test_df:
            alpha: 0.05 is default value, two-tail value

        Returns:
            Explanations:
            dfs = predictions.summary_frame(alpha = alpha)
            # how mean_ci is calculated:
            dfs["mean_ci_lower"] = dfs["mean"] - stats.t.ppf(1 - alpha / 2, results.df_resid) * dfs['mean_se']
            dfs["mean_ci_upper"] = dfs["mean"] + stats.t.ppf(1 - alpha / 2, results.df_resid) * dfs['mean_se']

            # how obs_ci is calculated:
            dfs["obs_ci_lower"] = dfs["mean"] - stats.t.ppf(1 - alpha / 2, results.df_resid) * np.sqrt(dfs['mean_se'] ** 2 + results.mse_resid)
        """
        if self.formula:
            predictions = self.results.get_prediction(test_df)
        else:
            X = test_df[self.regressors]
            # has_constant: https://stackoverflow.com/questions/36532529/add-constant-in-statsmodels-not-working
            predictions = self.results.get_prediction(sm.add_constant(X, has_constant = 'add'))

        summ = predictions.summary_frame(alpha = alpha)
        summ['obs_se'] = np.sqrt(summ['mean_se'] ** 2 + self.results.mse_resid)
        return summ[['mean', 'mean_se', 'obs_se', 'mean_ci_lower', 'mean_ci_upper', 'obs_ci_lower', 'obs_ci_upper']]

    @ property
    def params(self):
        return self.results.params