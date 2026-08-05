# Lab 03.5 — External Tables & BigLake (Data Lake on GCS)

## Objectives
- Query Parquet/CSV **directly in Cloud Storage** without loading.
- Create an external table and understand the BigLake model.
- Understand when external vs native tables are appropriate.

## 1. Simple external table (no BigLake enforcement)
```sql
CREATE OR REPLACE EXTERNAL TABLE cymbal_warehouse.taxi_trips_ext
OPTIONS (
  format = 'PARQUET',
  uris   = ['gs://cymbal-raw-*/taxi/*.parquet']
);
```
```sql
SELECT vendor_id, AVG(fare_amount) FROM cymbal_warehouse.taxi_trips_ext GROUP BY vendor_id;
```

## 2. BigLake table (adds IAM + security enforcement on the lake)
```bash
# BigLake tables add table-level security over external data.
bq mk --external_table_definition=@parquet_uris.json cymbal_warehouse.taxi_trips_lake
```
```json
{
  "sourceFormat": "PARQUET",
  "sourceUris": ["gs://cymbal-raw-*/taxi/*.parquet"]
}
```

## 3. Federated queries
```sql
-- Query a Google Sheet or GCS file without any table
SELECT * FROM EXTERNAL_QUERY('projects/<PROJECT_ID>/locations/us/connections/conn_id',
  'SELECT * FROM `gcp-data-engineering-course.cymbal_warehouse.taxi_trips`');
```

## Decision: external vs native

| | Native table | External (BigLake) |
|---|---|---|
| Data | stored in BigQuery | stays in GCS |
| Performance | best (Colossus) | good (reads from GCS) |
| Security | IAM + policy tags | BigLake row/column security |
| Use | warehouse workloads | data lake / open formats |

## Exam notes
- **BigLake** unifies warehouses and lakes: external tables over GCS with
  fine-grained security, metastore integration, and support for Iceberg/Delta/Parquet.
- External tables don't support clustering; partition pruning still works from Hive-style partitions.
