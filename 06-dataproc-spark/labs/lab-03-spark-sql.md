# Lab 06.3 — Spark SQL Job

## Objectives
- Run SQL directly against files in GCS and BigQuery.
- Understand Hive metastore usage.

## 1. SQL script (`code/taxi_analysis.sql`)
```sql
CREATE TEMPORARY VIEW taxi_trips
USING org.apache.spark.sql.parquet
OPTIONS (path "gs://cymbal-raw-<PROJECT>/taxi/*.parquet");

CREATE TEMPORARY VIEW vendor_stats AS
SELECT
  vendor_id,
  COUNT(*)        AS trip_count,
  AVG(fare_amount) AS avg_fare,
  SUM(fare_amount) AS total_revenue,
  AVG(trip_distance) AS avg_distance
FROM taxi_trips
WHERE fare_amount > 0
GROUP BY vendor_id;

SELECT * FROM vendor_stats ORDER BY total_revenue DESC;
```

## 2. Submit
```powershell
gcloud dataproc jobs submit spark-sql `
  --cluster=taxi-cluster `
  --region=us-central1 `
  --file=code/taxi_analysis.sql
```

## Exam notes
- Dataproc includes **Hive metastore**; tables persist across jobs.
- Use Spark SQL for complex SQL transformations; PySpark for custom code/ML.
- `gcloud dataproc jobs submit spark-sql` is the job-type for SQL files.
