import logging
import jaydebeapi

from AqDsKit.accessors.db.drivers import download_jdbc_jar


class dfConfJdbc:
    def __init__(self, driver: str):
        self.driver = driver
        self.jar_path = None


    def bindServer(self, ip: str, port: int, db: str):
        self.ip = ip
        self.port = port
        self.db = db

    def login(self, username: str, password: str):
        self.username = username
        self.password = password

    def argTempStr(self):
        raise NotImplementedError("Must implement this method to get different arg placeholder for different database")

    def getConnStr(self) -> str:
        raise NotImplementedError("Must implement this method to get connection string")

    def getConnection(self) -> jaydebeapi.Connection:
        conn = jaydebeapi.connect(
            jclassname = self.driver,
            url = self.getConnStr(),
            driver_args = [self.username, self.password],
            jars = self.jar_path
        )
        return conn



class HiveJdbc(dfConfJdbc):
    def __init__(self):
        super().__init__("org.apache.hive.jdbc.HiveDriver")

    def argTempStr(self):
        return "?"

    def getConnStr(self) -> str:
        return f"jdbc:hive2://{self.ip}:{self.port}/{self.db}"

    def prepare(self, jar_folder):
        jar_file_url = "https://repo1.maven.org/maven2/org/apache/hive/hive-jdbc/3.1.2/hive-jdbc-3.1.2.jar"
        self.jar_path = download_jdbc_jar(jar_file_url, jar_folder)


class PrestoJdbc(dfConfJdbc):
    def __init__(self):
        super().__init__("com.facebook.presto.jdbc.PrestoDriver")

    def argTempStr(self):
        return "?"

    def getConnStr(self) -> str:
        return f"jdbc:presto://{self.ip}:{self.port}/{self.db}"

    def prepare(self, jar_folder):
        jar_file_url = "https://repo1.maven.org/maven2/io/prestosql/presto-jdbc/347/presto-jdbc-347.jar"
        self.jar_path = download_jdbc_jar(jar_file_url, jar_folder)