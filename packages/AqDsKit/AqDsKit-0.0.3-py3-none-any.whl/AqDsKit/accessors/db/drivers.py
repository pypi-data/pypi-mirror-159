import logging
import os

import requests


def download_jdbc_jar(jar_file_url, jdbc_driver_folder, jar_file_name: str = None):
    if not os.path.exists(jdbc_driver_folder):
        os.makedirs(jdbc_driver_folder)

    if not jar_file_name:
        jar_file_name = jar_file_url.split('/')[-1]

    jar_path = os.path.join(jdbc_driver_folder, jar_file_name)

    proxies = {
        'http': os.getenv('HTTP_PROXY', None),
        'https': os.getenv('HTTPS_PROXY', None)
    }

    if proxies['http']:
        with requests.get(
                jar_file_url,
                proxies = proxies
        ) as response, open(jar_path, 'wb') as out_file:
            out_file.write(response.content)
    else:
        with requests.get(jar_file_url) as response, open(jar_path, 'wb') as out_file:
            out_file.write(response.content)

    logging.info(f"Successfully download JDBC jar from {jar_file_url} and saved to {jar_path}")
    return jar_path


def download_jdbc_jars(jdbc_driver_folder):
    jars = [
        {
            'db_provider': 'db2',
            'jar_file_url': 'https://repo1.maven.org/maven2/com/ibm/db2/jcc/db2jcc/db2jcc4/db2jcc-db2jcc4.jar',
            'jar_file_name': 'db2jcc-db2jcc4.jar'
        },
        {
            'db_provider': 'mysql',
            'jar_file_url': 'https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.27/mysql-connector-java-8.0.27.jar',
            'jar_file_name': 'mysql-connector-java.jar'
        },
        {
            'db_provider': 'sqlite',
            'jar_file_url': 'https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/3.36.0.3/sqlite-jdbc-3.36.0.3.jar',
            'jar_file_name': 'sqlite-jdbc.jar'
        },
        {
            'db_provider': 'sqlserver',
            'jar_file_url': 'https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/8.4.0.jre8/mssql-jdbc-8.4.0.jre8.jar',
            'jar_file_name': 'mssql-jdbc-8.4.0.jre8.jar'
        },
        {
            'db_provider': 'oracle',
            'jar_file_url': 'https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc8/19.3.0.0/ojdbc8-19.3.0.0.jar',
            'jar_file_name': 'ojdbc.jar'
        },
        {
            'db_provider': 'presto',
            'jar_file_url': 'https://repo1.maven.org/maven2/io/prestosql/presto-jdbc/347/presto-jdbc-347.jar',
            'jar_file_name': 'presto.jar'
        },
        {
            'db_provider': 'postgresql',
            'jar_file_url': 'https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.18/postgresql-42.2.18.jar',
            'jar_file_name': 'postgresql.jar'
        },
        {
            'db_provider': 'sas',
            'jar_file_url': 'https://repos.spark-packages.org/saurfang/spark-sas7bdat/3.0.0-s_2.12/spark-sas7bdat-3.0.0-s_2.12.jar',
            'jar_file_name': 'spark-sas.jar'
        },
        {
            'db_provider': 'parso',  # use to read sas dataset
            'jar_file_url': 'https://repo1.maven.org/maven2/com/epam/parso/2.0.14/parso-2.0.14.jar',
            'jar_file_name': 'parso.jar'
        }
    ]

    if not os.path.exists(jdbc_driver_folder):
        os.makedirs(jdbc_driver_folder)

    for jar in jars:
        db_provider = jar.get('db_provider')
        jar_file_url = jar.get('jar_file_url')
        jar_file_name = jar.get('jar_file_name')

        download_jdbc_jar(jar_file_url, jdbc_driver_folder, jar_file_name)