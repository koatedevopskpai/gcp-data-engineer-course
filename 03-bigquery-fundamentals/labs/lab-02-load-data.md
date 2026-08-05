# Lab 03.2 — Load CSV from Cloud Storage

## Objectives
- Load the taxi CSV from GCS into `taxi_trips` using three methods.
- Verify bytes scanned and load job errors.

## 1. `bq load`
```powershell
bq load `
  --source_format=CSV `
  --skip_leading_rows=1 `
  --autodetect `
  cymbal_warehouse.taxi_trips `
  gs://cymbal-raw-<PROJECT_ID>/taxi/taxi_trips.csv
```

## 2. SQL `LOAD DATA`
```sql
LOAD DATA INTO cymbal_warehouse.taxi_trips
FROM FILES (
  format = 'CSV',
  uris   = ['gs://cymbal-raw-*/taxi/*.csv'],
  skip_leading_rows = 1
);
```

## 3. Python client
```python
# code/load_csv.py
from google.cloud import bigquery

client = bigquery.Client()
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
)
uri = "gs://cymbal-raw-{}/taxi/taxi_trips.csv".format(client.project)
load_job = client.load_table_from_uri(uri, "cymbal_warehouse.taxi_trips", job_config=job_config)
load_job.result()
table = client.get_table("cymbal_warehouse.taxi_trips")
print(f"Loaded {table.num_rows} rows")
```

## Exam notes
- Load jobs are free; **query processing** is billed per TB scanned.
- `autodetect` infers schema; prefer explicit schema for production.
- Use `--null_marker`, `--field_delimiter`, `--quote`, `--encoding` for messy files.
- For very large files use Parquet/Avro (faster, compressed) instead of CSV.
