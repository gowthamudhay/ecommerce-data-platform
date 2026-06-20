import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

products = spark.read.option(
    "header",
    True
).csv("s3://ecommerce-data-platform-raw/products/")

products_clean = products.filter(
    col("price").cast("double") > 0
)

products_clean = products_clean.dropDuplicates()

products_clean.write.mode("overwrite").parquet("s3://ecommerce-data-platform-processed/products/")