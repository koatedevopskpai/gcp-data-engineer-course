# Lab 06.4 — BigQuery Connector with Spark

## Objectives
- Read directly from BigQuery into a Spark DataFrame.
- Transform and write back.

## 1. Script (`code/bigquery_spark_pipeline.py`)
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, sum

spark = SparkSession.builder.appName("BigQueryPipeline").getOrCreate()

df = (
    spark.read.format("bigquery")
    .option("table", "cymbal_warehouse.taxi_trips")
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
    .option("table", "cymbal_warehouse.vendor_aggregates") \
    .option("writeMethod", "direct") \
    .mode("overwrite") \
    .save()

spark.stop()
```

## 2. Submit
```powershell
gcloud dataproc jobs submit pyspark code\bigquery_spark_pipeline.py `
  --cluster=taxi-cluster `
  --region=us-central1 `
  --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar
```

## Exam notes
- Reading BigQuery into Spark is for **large-scale custom processing / ML feature
  engineering**; if only SQL aggregation is needed, stay in BigQuery.
- The connector queries via the BigQuery Storage API (fast parallel reads).
