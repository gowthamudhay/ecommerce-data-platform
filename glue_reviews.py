import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

reviews = spark.read.option(
    "header",
    True
).csv("s3://ecommerce-data-platform-raw/reviews/")

reviews_clean = reviews.filter(
    (col("rating").cast("int") >= 1) &
    (col("rating").cast("int") <= 5))
    
reviews_clean = reviews_clean.dropDuplicates()

reviews_clean.write.mode("overwrite").parquet("s3://ecommerce-data-platform-processed/reviews/")