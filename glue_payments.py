import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

payments = spark.read.option(
    "header",
    True
).csv("s3://ecommerce-data-platform-raw/payments/")

payments_clean = payments.filter(
    col("amount").cast("double") > 0)
    
payments_clean = payments_clean.dropDuplicates()

payments_clean.write.mode("overwrite").parquet("s3://ecommerce-data-platform-processed/payments/")