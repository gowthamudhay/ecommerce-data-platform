import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

orders = spark.read.option(
    "header",
    True
).csv("s3://ecommerce-data-platform-raw/orders/"
)

orders_clean = orders.dropna()
orders_clean = orders_clean.dropDuplicates()

orders_clean = orders_clean.withColumn("quantity", col("quantity").cast("int"))

orders_clean = orders_clean.filter(col("quantity") > 0)


orders_clean.write.mode("overwrite").option("header", True).parquet("s3://ecommerce-data-platform-processed/orders/")

print("Orders ETL Completed")