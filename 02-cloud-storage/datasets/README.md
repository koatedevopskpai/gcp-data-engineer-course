# Module 02 — Datasets

Data files referenced by this module and the rest of the course.

## Canonical taxi dataset (in this repo)

`taxi_trips.csv` — 40 curated NYC-style yellow taxi trip rows with a header
matching `03-bigquery-fundamentals/code/schema.json` exactly:

| Column | Type | Notes |
|---|---|---|
| `trip_id` | STRING | REQUIRED in schema.json |
| `vendor_id` | STRING | `VTS` / `VCM` |
| `pickup_datetime` | TIMESTAMP | first 5 columns are positional for the Dataflow `ParseCSV` |
| `fare_amount` | FLOAT64 | |
| `trip_distance` | FLOAT64 | |
| `dropoff_datetime` | TIMESTAMP | |
| `passenger_count` | INT64 | |
| `tip_amount` | FLOAT64 | |
| `total_amount` | FLOAT64 | |
| `payment_type` | STRING | `CREDIT` / `CSH` / `DEBIT` / `NO` |
| `pickup_location` | STRING | |
| `dropoff_location` | STRING | |

> The first five columns are ordered `trip_id, vendor_id, pickup_datetime,
> fare_amount, trip_distance` because `05-dataflow-beam/code/taxi_etl_pipeline.py`
> parses rows positionally (`row[0..4]`) and `06-dataproc-spark/code/taxi_analysis.py`
> reads them by header name.
>
> `03-bigquery-fundamentals/code/schema.json` is ordered to match this header
> exactly, so `bq load ... schema.json` maps columns correctly (BigQuery matches
> explicit schemas positionally when loading CSV).

### Upload to your raw bucket (Modules 3, 5, 6 depend on this)

```bash
# from the repo root
gsutil cp 02-cloud-storage/datasets/taxi_trips.csv \
  gs://cymbal-raw-<PROJECT_ID>/taxi/taxi_trips.csv
```

```powershell
# PowerShell equivalent
gsutil cp 02-cloud-storage\datasets\taxi_trips.csv `
  gs://cymbal-raw-<PROJECT_ID>/taxi/taxi_trips.csv
```

## Optional: real NYC TLC data (larger dataset)

The New York City TLC yellow-taxi trip records are public. A monthly Parquet
file (e.g. January 2024) is published from the TLC CDN:

```bash
gsutil cp https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet \
  gs://cymbal-raw-<PROJECT_ID>/taxi_trips/yellow_tripdata_2024-01.parquet
```

> Note: real TLC files use different column names (`VendorID`, `tpep_pickup_datetime`,
> `PULocationID`, ...) and have **no `trip_id`**. They are fine for the Module 3
> BigLake/external-table and Module 2 transfer labs, but the Modules 5/6 taxi
> pipelines expect the curated `taxi_trips.csv` header. The previously documented
> path `gs://nyc-tlc/misc/taxi_trip_data.parquet` is no longer accessible.

## sample-transactions

`gs://cloud-samples-data/bigquery/sample-transactions/` — Google-hosted sample
CSV used for the upload/transfer labs (`02-cloud-storage/labs/lab-02`, `lab-05`).

## Query-only public datasets

The `bigquery-public-data.*` datasets are queried directly (Module 3+), never
downloaded.
