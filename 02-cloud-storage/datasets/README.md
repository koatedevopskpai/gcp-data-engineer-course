# Module 02 — Datasets

Public datasets referenced by this module (no download needed for most):

| Dataset | Where | Used for |
|---|---|---|
| NYC TLC taxi trip records (CSV) | `gs://cloud-samples-data/` and nyc-tlc public bucket | upload/transfer labs |
| sample-transactions | `gs://cloud-samples-data/bigquery/sample-transactions/` | quick upload/load labs |

To fetch the NYC TLC data used in later modules:

```bash
gsutil -m cp -r gs://nyc-tlc/misc/taxi_trip_data.parquet gs://cymbal-raw-<PROJECT_ID>/taxi/
```

> The `bigquery-public-data.*` datasets are queried directly (Module 3+), never downloaded.
