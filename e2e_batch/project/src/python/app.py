# Import reader and loader
from DBReader import reader
from DBWriter import writer

from pyspark.sql import SparkSession
spark = SparkSession.builder.config("spark.jars", "/opt/project/resources/connectors/mysql-connector-j-8.0.32.jar").getOrCreate()

# Import sql functions
from pyspark.sql.functions import *
