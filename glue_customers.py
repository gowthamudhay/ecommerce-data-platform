import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

customers = spark.read.option(
    "header",
    True
).csv("s3://ecommerce-data-platform-raw/customers/")

customers_clean = customers.dropna()
customers_clean = customers_clean.dropDuplicates()

customers_clean.write.mode("overwrite").parquet("s3://ecommerce-data-platform-processed/customers/")