# Lab 03.1 — Create Dataset and Partitioned/Clustered Table

## Objectives
- Create the `cymbal_warehouse` dataset.
- Create a column-partitioned, clustered `taxi_trips` table with an explicit schema.
- Understand ingestion-time vs column partitioning.

## Steps

```sql
-- 1. Create the dataset (schema = dataset alias in BigQuery)
CREATE SCHEMA cymbal_warehouse
OPTIONS (
  location = 'us-central1',
  default_table_expiration_days = 365
);
```

```sql
-- 2. Create a partitioned + clustered table
CREATE TABLE cymbal_warehouse.taxi_trips (
  trip_id          STRING,
  vendor_id        STRING,
  pickup_datetime  TIMESTAMP,
  dropoff_datetime TIMESTAMP,
  pickup_location  STRING,
  dropoff_location STRING,
  trip_distance    FLOAT64,
  fare_amount      FLOAT64,
  tip_amount       FLOAT64,
  total_amount     FLOAT64,
  payment_type     STRING,
  passenger_count  INT64
)
PARTITION BY DATE(pickup_datetime)          -- column-based partitioning
CLUSTER BY vendor_id, payment_type;         -- clustering for correlated scans
```

CLI equivalent:
```powershell
bq mk --dataset cymbal_warehouse
bq mk --table `
  --schema=schema.json `
  --time_partitioning_field=pickup_datetime `
  --time_partitioning_type=DAY `
  --clustering_fields=vendor_id,payment_type `
  cymbal_warehouse.taxi_trips
```

## Partitioning types (exam-critical)
- **Ingestion-time** (`_PARTITIONTIME` pseudo-column): partitions by the time the
  data is loaded. No timestamp column required.
- **Column-based** (`PARTITION BY DATE(col)`): partitions by values in a
  TIMESTAMP/DATE/DATETIME column. Queryable and filterable directly.
- **Integer-range partitioning** (`PARTITION BY RANGE_BUCKET(col, [...])`): for
  integer columns.

## Exam notes
- Partitioning prunes **entire partitions**; clustering prunes **blocks within
  partitions**. Partitioning first, clustering second.
- Maximum partitions per table: 10,000 (integer/date/time range). Wildcard
  `events_*` tables partition by `_TABLE_SUFFIX` — same 10k limit across tables.
