#!/usr/bin/env python
"""PySpark job: aggregate taxi trips by vendor and write to BigQuery."""
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, max, min, sum

PROJECT = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")

spark = SparkSession.builder.appName("TaxiAnalysis").getOrCreate()

df = spark.read.option("header", True).csv(f"gs://cymbal-raw-{PROJECT}/taxi/*.csv")

result = (
    df.filter(col("fare_amount") > 0)
    .groupBy("vendor_id")
    .agg(
        count("*").alias("trip_count"),
        avg("fare_amount").alias("avg_fare"),
        sum("fare_amount").alias("total_revenue"),
        max("trip_distance").alias("max_distance"),
        min("trip_distance").alias("min_distance"),
    )
)

result.write.format("bigquery") \
    .option("table", f"{PROJECT}.cymbal_warehouse.taxi_vendor_stats") \
    .option("writeMethod", "direct") \
    .mode("overwrite") \
    .save()

spark.stop()
