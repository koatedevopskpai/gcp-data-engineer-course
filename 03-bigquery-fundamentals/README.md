# Module 03 — BigQuery Fundamentals

Load data into BigQuery, model it, query it, and reason about cost/slots.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-dataset-table.md` | Create dataset + tables |
| `labs/lab-02-load-data.md` | Load CSV with `bq load` and `load_csv.py` |
| `labs/lab-03-analytical-queries.md` | Analytic SQL: joins, aggregation, `WHERE` |
| `labs/lab-04-public-datasets.md` | Query public datasets |
| `labs/lab-05-external-biglake.md` | External tables + BigLake |
| `labs/lab-06-slots-cost.md` | Slots, pricing, on-demand vs capacity |
| `code/schema.json` | Table schema (order matches CSV header exactly) |
| `code/load_csv.py` | Python `google-cloud-bigquery` loader (autodetect or schema) |
| `exercises/exercises.md` | Self-check questions |

## Data contract

`schema.json` field order is **positional** — `bq load` maps CSV columns by
position, so the schema is kept in exact CSV-header order
(`trip_id, vendor_id, pickup_datetime, fare_amount, trip_distance`).

## TL;DR

```bash
bq mk cymbal_warehouse
bq load --autodetect cymbal_warehouse.taxi_trips \
  gs://cymbal-raw-YOUR_PROJECT_ID/taxi/taxi_trips.csv
# or the Python loader:
python 03-bigquery-fundamentals/code/load_csv.py
```

## Exam notes

- BigQuery separates **storage** and **compute (slots)**; on-demand bills bytes
  scanned, capacity mode reserves slots.
- **Autodetect vs explicit schema**: autodetect is fast for demos; production
  loads pin a schema. Positional mapping is why column order matters on CSV loads.
- Partitioning (date) and clustering (high-cardinality) are the cost/performance
  levers for large tables.
