import logging
import os
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf


# os.environ['PYSPARK_PYTHON'] = 'python3.8'
# os.environ['PYSPARK_DRIVER_PYTHON'] = 'python3.8'
from AqDsKit.accessors.db.dbconfigs import baseDbInf
from AqDsKit.accessors.db.drivers import download_jdbc_jars
from AqDsKit.accessors.fs.s3 import S3Configs
from AqDsKit.utils.custom_structures import EnhancedDict


class SparkConnector:

    @ classmethod
    def setup(cls, s3_config: S3Configs, jdbc_driver_folder : str = os.getcwd()):
        """set up for the environment to urn successfully

        :param jdbc_driver_folder: folder path to save the jdbc drivers
        :return:
        """

        cls.STORAGE_URL = s3_config.endpoint_url
        cls.ACCESS_KEY = s3_config.aws_access_key_id
        cls.SECRET_ACCESS_KEY = s3_config.aws_secret_access_key
        cls.SESSION_TOKEN = s3_config.aws_session_token

        # download jdbc
        download_jdbc_jars(jdbc_driver_folder)
        cls.JAR_PATHS = ":".join(os.path.join(jdbc_driver_folder, jar) for jar in os.listdir(jdbc_driver_folder))
        logging.info(f"JDBC Driver Jars: {cls.JAR_PATHS}")

        ## build the configs
        cls.conf = EnhancedDict()
        cls.conf["spark.hadoop.fs.s3a.endpoint"] = cls.STORAGE_URL
        cls.conf["spark.hadoop.fs.s3a.aws.credentials.provider"] = 'org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider'
        cls.conf["spark.hadoop.fs.s3a.access.key"] = cls.ACCESS_KEY
        cls.conf["spark.hadoop.fs.s3a.secret.key"] = cls.SECRET_ACCESS_KEY
        cls.conf["spark.hadoop.fs.s3a.session.token"] = cls.SESSION_TOKEN
        cls.conf["spark.hadoop.fs.s3a.fast.upload"] = True
        cls.conf["spark.hadoop.fs.s3a.path.style.access"] = True
        cls.conf["spark.hadoop.fs.s3a.impl"] = "org.apache.hadoop.fs.s3a.S3AFileSystem"
        cls.conf["spark.hadoop.fs.s3a.multipart.size"] = "128M"
        cls.conf["spark.hadoop.fs.s3a.fast.upload.active.blocks"] = 8
        cls.conf["spark.driver.extraClassPath"] = cls.JAR_PATHS

    @ classmethod
    def getSparkSession(cls, app_name : str = "SparkConnector", master : str = "local"):

        sparkSessionBuilder = SparkSession.builder.master(master).appName(app_name)
        for k, v in cls.conf.items():
            sparkSessionBuilder = sparkSessionBuilder.config(k, v)

        spark = sparkSessionBuilder.getOrCreate()

        return spark

    def __init__(self, app_name : str = "SparkConnector", master : str = "local"):
        if not hasattr(self, 'JAR_PATHS'):
            raise Exception("Must call SparkConnector.setup() before initialization")

        self.spark = self.getSparkSession(app_name, master)
        logging.info(f"Spark session object successfully created, call SparkConnector({app_name}).spark to get spark obj")

    def get_file_path(self, path: str) -> str:
        return path

    def get_common_reader(self, header=True, sep=",", schema=None):
        if schema:
            return self.spark.read.option('header', header) \
                .option("inferSchema", "false") \
                .option("sep", sep) \
                .schema(schema)
        else:
            return self.spark.read.option('header', header) \
                .option("inferSchema", "true") \
                .option("sep", sep)

    def read_csv(self, *path: str, header=True, sep=",", schema=None):
        # path = self.get_file_path(path)

        try:
            df = self.get_common_reader(header, sep, schema).csv(*path)
        except Exception as e:
            logging.error('File Load FAILED: ' + str(e))
        else:
            logging.info('File Load successfully.')
            return df

    def read_sas(self, path: str):
        # path = self.get_file_path(path)

        try:
            df = self.spark.read.format("com.github.saurfang.sas.spark").load(path)
        except Exception as e:
            logging.error('File Load FAILED: ' + str(e))
        else:
            logging.info('File Load successfully.')
            return df

    def read_parquet(self, *path: str, header=True, sep=",", schema=None):
        # path = self.get_file_path(path)

        try:
            df = self.get_common_reader(header, sep, schema).parquet(*path)
        except Exception as e:
            logging.error('File Load FAILED: ' + str(e))
        else:
            logging.info('File Load successfully.')
            return df

    def save_csv(self, df, path: str, header=True, sep=",", mode="overwrite", repartition: int = None):
        path = self.get_file_path(path)

        if repartition:
            df = df.repartition(repartition)

        try:
            df.write.option('header', header).option("sep", sep).mode(mode).csv(path)
        except Exception as e:
            logging.error('File Wrote FAILED: ' + str(e))
        else:
            logging.info('File Wrote successfully.')

    def save_parquet(self, df, path: str, header=True, sep=",", mode="overwrite", repartition: int = None):
        path = self.get_file_path(path)

        if repartition:
            df = df.repartition(repartition)

        try:
            df.write.option('header', header).option("sep", sep).mode(mode).parquet(path)
        except Exception as e:
            logging.error('File Wrote FAILED: ' + str(e))
        else:
            logging.info('File Wrote successfully.')

    def query_db(self, dbConf: baseDbInf, sql: str, result_name: str = "temp_df", **kws):
        """query from database and return spark dataframe

        :param dbConf: the dbConf object for connection string setup
        :param sql: the sql query to make
        :param result_name: spark jdbc requires each query result to have a table name
        :param kws: other parameters that could parse into .jdbc(properties)
        :return: spark DataFrame
        """

        sql = f"({sql.replace(';', '')}) as {result_name}"  # drop ; and wrap with temp table name
        properties = {
            "driver": dbConf.getDriverClass(),
            # "dbtable" : sql,
        }

        if hasattr(dbConf, 'username'):
            properties["user"] = dbConf.username
            properties["password"] = dbConf.password

        for k, v in kws.items():
            properties[k] = v

        try:
            df = self.spark.read.jdbc(
                url=dbConf.getJdbcUrl(),
                table=sql,
                properties=properties
            )
        except Exception as e:
            logging.error('Query Load FAILED: ' + str(e))
        else:
            logging.info('Query Load successfully.')
            return df

    def save_db(self, dbConf: baseDbInf, df, table_name: str, mode: str = None, column_schema: dict = None,
                **kws) -> int:
        """save df to database

        :param dbConf: the dbConf object for connection string setup
        :param df: spark dataframe to save
        :param table_name: name of the table in the database
        :param mode: {None, append, overwrite}, None will fail if table exists, append will append to end, overwrite will discard existing values
        :param column_schema: dictionary of column and dtype, e.g. column_schema = {"cur" : "varchar(4)", "v1": "float"}
        :param kws: other parameters that could parse into .jdbc(properties)
        :return: 1 for success and 0 for failed
        """
        properties = {
            "driver": dbConf.getDriverClass(),
            "dbtable": table_name,
        }

        if hasattr(dbConf, 'username'):
            properties["user"] = dbConf.username
            properties["password"] = dbConf.password

        if column_schema:
            col_sch = ",".join(f"{k} {v}" for k, v in column_schema.items())
            properties["createTableColumnTypes"] = col_sch

        for k, v in kws.items():
            properties[k] = v

        try:
            df.write.jdbc(
                url=dbConf.getJdbcUrl(),
                table=table_name,
                mode=mode,
                properties=properties
            )
        except Exception as e:
            logging.error('Save to DB FAILED: ' + str(e))
            return 0
        else:
            logging.info('Save to DB successfully.')
            return 1