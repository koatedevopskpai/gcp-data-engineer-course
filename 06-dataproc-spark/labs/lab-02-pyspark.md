# Lab 06.2 — PySpark: GCS → Aggregations → BigQuery

## Objectives
- Read CSV/Parquet from Cloud Storage into a Spark DataFrame.
- Aggregate by vendor.
- Write results to BigQuery with the BigQuery connector.

## 1. Script (`code/taxi_analysis.py`)
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, max, min, sum

spark = SparkSession.builder.appName("TaxiAnalysis").getOrCreate()

df = spark.read.option("header", True).csv("gs://cymbal-raw-<PROJECT>/taxi/*.csv")

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
    .option("table", "cymbal_warehouse.taxi_vendor_stats") \
    .option("writeMethod", "direct") \
    .mode("overwrite") \
    .save()

spark.stop()
```

## 2. Submit
```powershell
gcloud dataproc jobs submit pyspark code\taxi_analysis.py `
  --cluster=taxi-cluster `
  --region=us-central1 `
  --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar
```

## Exam notes
- The **BigQuery connector** lets Spark read/write BigQuery without copying all
  data through the driver (`writeMethod=direct` uses the Storage Write API).
- Cloud Storage connector: use `gs://` URIs natively.
- `spark-bigquery-latest_2.12.jar` must match your Spark/Scala version.
