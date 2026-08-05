#!/usr/bin/env python
"""Read BigQuery into Spark, aggregate, write back."""
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, sum

PROJECT = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")

spark = SparkSession.builder.appName("BigQueryPipeline").getOrCreate()

df = (
    spark.read.format("bigquery")
    .option("table", f"{PROJECT}.cymbal_warehouse.taxi_trips")
    .load()
)

result = (
    df.filter(col("fare_amount") > 0)
    .groupBy("vendor_id")
    .agg(
        count("*").alias("trip_count"),
        avg("fare_amount").alias("avg_fare"),
        sum("fare_amount").alias("total_revenue"),
    )
)

result.write.format("bigquery") \
    .option("table", f"{PROJECT}.cymbal_warehouse.vendor_aggregates") \
    .option("writeMethod", "direct") \
    .mode("overwrite") \
    .save()

spark.stop()
