# Lab 03.3 — Analytical Queries with Partition Pruning

## Objectives
- Write analytical queries that benefit from partition pruning.
- Confirm cost savings via `--dry_run` and job statistics.

## Steps

```sql
-- Query that prunes to a single month's partition
SELECT
  DATE(pickup_datetime) AS trip_date,
  COUNT(*)              AS total_trips,
  AVG(fare_amount)      AS avg_fare,
  SUM(total_amount)     AS total_revenue
FROM cymbal_warehouse.taxi_trips
WHERE pickup_datetime >= '2024-01-01'
  AND pickup_datetime  <  '2024-02-01'
GROUP BY trip_date
ORDER BY trip_date;
```

```sql
-- Clustering helps equality filters on vendor_id
SELECT vendor_id, AVG(fare_amount) AS avg_fare, COUNT(*) AS trips
FROM cymbal_warehouse.taxi_trips
WHERE vendor_id = 'VTS'
GROUP BY vendor_id;
```

## Cost check (no data billed)
```powershell
bq query --dry_run --use_legacy_sql=false `
  "SELECT COUNT(*) FROM cymbal_warehouse.taxi_trips WHERE pickup_datetime >= '2024-01-01' AND pickup_datetime < '2024-02-01'"
```

In the console, the **Execution details** tab shows bytes billed and slot time.

## Exam notes
- Filters on the partitioning column are what make queries cheap. Filtering on a
  non-partition column scans everything.
- `TIMESTAMP` filters should use `>=` / `<` (half-open ranges) to capture full days.
