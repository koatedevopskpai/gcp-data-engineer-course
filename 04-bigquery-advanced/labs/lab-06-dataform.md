# Lab 04.6 — Dataform: SQL Pipelines as Code

## Objectives
- Understand Dataform (Git-backed SQL pipelines for BigQuery).
- Create a Dataform repository and a staging + mart model.
- Run `dataform compile`/`run` and see the generated SQL.

## Concepts
Dataform brings software-engineering practices to SQL:
- **Table definitions** in `.sqlx` files with config headers
- **Incremental** and **full refresh** strategies
- **Dependencies** via `ref()` — automatic DAG building
- **Assertions** for data quality (`data_quality` blocks)

## 1. Create a repository (console or REST API)

> **Erratum:** there is **no** `gcloud dataform` command group in the current
> Cloud SDK. Create repositories in the console, or via the Dataform REST API.

**Option A — Console (recommended):** Console → Dataform → **Create repository**
→ Repository ID `cymbal-dataform` → region `us-central1` → service account → **Create**.

**Option B — REST API** (needs `roles/dataform.admin` and an authenticated shell):
```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  -d '{}' \
  "https://dataform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/us-central1/repositories?repositoryId=cymbal-dataform"
```

Both require the API first:
```bash
gcloud services enable dataform.googleapis.com
```
Then connect a Git repo (GitHub/GitLab) in the console UI and push the project in `code/dataform/`.

## 2. Project layout (see `code/dataform/`)
```
definitions/
├── staging/stg_taxi.sqlx
├── marts/fct_daily_sales.sqlx
└── assertions/stg_taxi_assertions.sqlx
```

## 3. Example model
```sqlx
-- code/dataform/definitions/staging/stg_taxi.sqlx
config {
  type: "table",
  schema: "staging",
  partition_by: "trip_date"
}
SELECT
  trip_id,
  DATE(pickup_datetime) AS trip_date,
  vendor_id,
  fare_amount,
  trip_distance
FROM ${ref("cymbal_warehouse", "taxi_trips")}
WHERE fare_amount > 0
```

```sqlx
-- code/dataform/definitions/marts/fct_daily_sales.sqlx
config {
  type: "table",
  schema: "marts"
}
SELECT
  trip_date,
  vendor_id,
  COUNT(*)        AS trips,
  SUM(fare_amount) AS revenue
FROM ${ref("stg_taxi")}
GROUP BY trip_date, vendor_id
```

## 4. Run
```bash
npm i -g @dataform/cli
dataform install
dataform compile
dataform run
```

## Exam notes
- Dataform is the recommended "dbt-like" tool **inside BigQuery** for versioned
  SQL; dbt also works via the BigQuery adapter (used in Module 11).
- Both support `ref()` dependency resolution, incremental models, and tests.
