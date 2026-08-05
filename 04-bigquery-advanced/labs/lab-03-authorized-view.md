# Lab 04.3 — Authorized Views (CORRECTED)

> **Erratum:** the original draft showed `bq show --view --authorized_view ...` and
> `GRANT SELECT ... TO "user:..."`. Neither is valid BigQuery syntax. The correct
> mechanism is to **authorize the view on its dataset**: users who hold access on the
> *view's dataset* (or the view itself) can query it without ever seeing the underlying table.

## Objective
Give the marketing team a restricted subset of `taxi_trips` (only trips > $10,
no payment/passenger columns) **without granting them access to the base table**.

## 1. Create the view (in the same or a separate dataset)

```sql
CREATE VIEW cymbal_warehouse.marketing_trip_view AS
SELECT
  trip_id,
  pickup_datetime,
  pickup_location,
  dropoff_location,
  trip_distance,
  fare_amount
FROM cymbal_warehouse.taxi_trips
WHERE fare_amount > 10;
```

## 2. Authorize the view (dataset-level access)

**Console:**
1. BigQuery → `cymbal_warehouse` dataset → **Share**
2. **Authorize views** → Add view → select `marketing_trip_view`

**CLI:** authorized views are written into the dataset's access list as
`view:` entries. You can add one via the `bq update` access JSON or the API:
```bash
bq show --format=prettyjson cymbal_warehouse > ds.json
# add: {"view": "projects/<PROJECT_ID>/datasets/cymbal_warehouse/tables/marketing_trip_view"} to "access"
bq update --source=ds.json cymbal_warehouse
```

## 3. Grant users access to the view (not the base table)

```bash
# Give the marketing group the ability to query the view + run jobs
gcloud projects add-iam-policy-binding <PROJECT_ID> \
  --member="group:marketing@example.com" \
  --role="roles/bigquery.dataViewer"

gcloud projects add-iam-policy-binding <PROJECT_ID> \
  --member="group:marketing@example.com" \
  --role="roles/bigquery.jobUser"

# Ensure they do NOT hold roles/bigquery.dataViewer on the base dataset's tables
# (per-dataset/table grants are more restrictive).
```

Marketing can now run:
```sql
SELECT * FROM cymbal_warehouse.marketing_trip_view;   -- works
SELECT payment_type FROM cymbal_warehouse.taxi_trips; -- denied (no table access)
```

## Alternative: row-level security
If you need row-level filtering without a view:
```sql
CREATE ROW ACCESS POLICY marketing_filter
ON cymbal_warehouse.taxi_trips
GRANT TO ("group:marketing@example.com")
FILTER USING (fare_amount > 10);
```

## Exam notes
- **Authorized views** = "share a subset without sharing the table". Views run
  with the **view creator's** credentials.
- Column-level security uses **policy tags** (Module 10), not views.
- Grants are IAM-based (`roles/bigquery.*`), not SQL `GRANT SELECT ... TO "user:"` (which is not BigQuery SQL).
