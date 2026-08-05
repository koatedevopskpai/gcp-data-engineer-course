# Lab 03.4 — Query Public Datasets

## Objectives
- Query `bigquery-public-data` datasets directly (no loading).
- Analyze the GA4 e-commerce sample and Chicago taxi trips.

## 1. GA4 e-commerce — daily users
```sql
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) AS unique_users,
  COUNT(*)                       AS total_events
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
GROUP BY event_date
ORDER BY event_date;
```

## 2. Chicago taxi — average trip duration by payment type
```sql
SELECT
  payment_type,
  AVG(TIMESTAMP_DIFF(trip_end_timestamp, trip_start_timestamp, MINUTE)) AS avg_duration_mins,
  COUNT(*) AS trip_count
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
WHERE trip_start_timestamp >= '2024-01-01'
  AND trip_start_timestamp  <  '2024-04-01'
GROUP BY payment_type
ORDER BY trip_count DESC;
```

## Exam notes
- **Wildcard tables** `events_*` + `_TABLE_SUFFIX` is the standard way to query
  partitioned GA4 / analytics exports.
- Queries against public datasets bill **your** project's on-demand tier
  (1 TB/month free tier covers course usage).

## Public datasets used across the course
- `bigquery-public-data.ga4_obfuscated_sample_ecommerce`
- `bigquery-public-data.chicago_taxi_trips`
- `bigquery-public-data.crypto_ethereum` (Module 4)
