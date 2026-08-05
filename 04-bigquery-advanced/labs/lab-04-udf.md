# Lab 04.4 — User-Defined Functions (SQL and JavaScript)

## Objectives
- Write a SQL UDF for currency normalization.
- Write a JS UDF for timestamp formatting.
- Call UDFs inside queries.

## 1. SQL UDF
```sql
CREATE OR REPLACE FUNCTION cymbal_warehouse.normalize_currency(
  amount FLOAT64,
  from_currency STRING,
  to_currency STRING
) RETURNS FLOAT64 AS (
  CASE
    WHEN from_currency = 'USD' AND to_currency = 'EUR' THEN amount * 0.85
    WHEN from_currency = 'USD' AND to_currency = 'GBP' THEN amount * 0.73
    ELSE amount
  END
);
```

## 2. JavaScript UDF
```sql
CREATE OR REPLACE FUNCTION cymbal_warehouse.format_timestamp_js(ts TIMESTAMP)
RETURNS STRING
LANGUAGE js AS """
  var d = new Date(ts);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  return d.getUTCDate() + ' ' + months[d.getUTCMonth()] + ' ' + d.getUTCFullYear();
""";
```

## 3. Use the UDFs
```sql
SELECT
  trip_id,
  cymbal_warehouse.format_timestamp_js(pickup_datetime) AS formatted_date,
  cymbal_warehouse.normalize_currency(fare_amount, 'USD', 'EUR') AS fare_eur
FROM cymbal_warehouse.taxi_trips
LIMIT 10;
```

## Exam notes
- **JS UDFs cannot be used inside `GROUP BY` or `ORDER BY`** clauses.
- JS UDFs have a 1 MB input/output limit per row (a real exam fact).
- UDFs persist in the dataset; `CREATE TEMP FUNCTION` is session-only.
- BigQuery supports remote UDFs (Cloud Functions/Cloud Run) for heavier logic.
