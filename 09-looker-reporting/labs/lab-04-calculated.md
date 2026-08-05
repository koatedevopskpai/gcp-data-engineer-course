# Lab 09.4 — Calculated Fields

## Objectives
- Add calculated fields and use them in charts.

## Fields to create (Data source → Add a field)
```text
Revenue per mile:  fare_amount / trip_distance

Trip category:
  CASE
    WHEN trip_distance < 5  THEN 'Short'
    WHEN trip_distance < 20 THEN 'Medium'
    ELSE 'Long'
  END

Tip rate:
  tip_amount / total_amount
```

## Steps
1. Data source → **Add a field** → enter name + formula.
2. Use the fields in charts/tables (e.g., avg revenue-per-mile by vendor).

## Exam notes
- Calculated fields run in the data source (BigQuery) context, not the browser.
