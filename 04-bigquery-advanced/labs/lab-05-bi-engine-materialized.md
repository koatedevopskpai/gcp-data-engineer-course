# Lab 04.5 — Materialized Views and BI Engine

## Objectives
- Create a materialized view to pre-aggregate daily taxi counts.
- Create a BI Engine reservation to accelerate dashboards.
- Inspect BI Engine usage.

## 1. Materialized view
```sql
CREATE MATERIALIZED VIEW cymbal_warehouse.daily_trip_counts
PARTITION BY trip_date
AS
SELECT
  DATE(pickup_datetime) AS trip_date,
  vendor_id,
  COUNT(*)              AS trip_count,
  SUM(fare_amount)      AS total_fare
FROM cymbal_warehouse.taxi_trips
GROUP BY DATE(pickup_datetime), vendor_id;
```
```sql
SELECT * FROM cymbal_warehouse.daily_trip_counts WHERE trip_date = '2024-01-15';
```

## 2. BI Engine reservation
Console: **BigQuery → BI Engine → Create reservation**
- Location: `us-central1`, capacity: 5 GB (1 GB minimum).

Verify:
```sql
SELECT project_id, reservation_name, location, size_gb
FROM `region-us-central1`.INFORMATION_SCHEMA.BI_CAPACITIES;
```
Check which queries used BI Engine:
```sql
SELECT query, total_slot_ms, bi_engine_statistics
FROM `region-us-central1`.INFORMATION_SCHEMA.JOBS
WHERE bi_engine_statistics IS NOT NULL
LIMIT 10;
```

## Exam notes
- **BI Engine** accelerates dashboard queries on data **already in BigQuery**;
  it is memory, not storage. Ideal for Looker Studio.
- **Materialized views** are auto-refreshed and cost less than re-running the
  query; they cannot be updated directly (BigQuery refreshes them).
- BigQuery **Connector/ODBC/JDBC** topics also appear — BI Engine pairs with them.
