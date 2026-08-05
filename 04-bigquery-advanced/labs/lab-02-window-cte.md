# Lab 04.2 — Window Functions and CTEs

## Objectives
- Compute running totals and moving averages with window functions.
- Use CTEs to structure multi-step analytics.
- Rank within groups with `RANK`/`DENSE_RANK`.

## Running total + 7-day average
```sql
WITH daily_sales AS (
  SELECT
    DATE(pickup_datetime) AS sale_date,
    SUM(total_amount)     AS daily_revenue
  FROM cymbal_warehouse.taxi_trips
  GROUP BY DATE(pickup_datetime)
)
SELECT
  sale_date,
  daily_revenue,
  SUM(daily_revenue) OVER (ORDER BY sale_date)                          AS running_total,
  AVG(daily_revenue) OVER (ORDER BY sale_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS seven_day_avg,
  LAG(daily_revenue, 1) OVER (ORDER BY sale_date)                       AS prev_day
FROM daily_sales
ORDER BY sale_date;
```

## Ranking within a group
```sql
SELECT
  vendor_id,
  DATE(pickup_datetime) AS trip_date,
  SUM(total_amount)     AS daily_revenue,
  RANK() OVER (PARTITION BY vendor_id ORDER BY SUM(total_amount) DESC) AS rank_in_vendor
FROM cymbal_warehouse.taxi_trips
GROUP BY vendor_id, DATE(pickup_datetime);
```

## 7-day moving average over transaction volume (crypto dataset)
```sql
SELECT
  DATE(block_timestamp) AS day,
  COUNT(*)              AS tx_count,
  AVG(COUNT(*)) OVER (ORDER BY DATE(block_timestamp) ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7d
FROM `bigquery-public-data.crypto_ethereum.transactions`
WHERE DATE(block_timestamp) >= '2024-01-01'
GROUP BY DATE(block_timestamp)
ORDER BY day;
```

## Exam notes
- Window functions cannot be used in `WHERE` — use a CTE/subquery.
- `ROWS BETWEEN ... AND ...` vs `RANGE` — know the frame syntax.
- `RANK` leaves gaps; `DENSE_RANK` does not; `ROW_NUMBER` is unique per row.
