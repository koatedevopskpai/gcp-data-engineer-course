-- Module 04 - SQL scripts

-- lab-01: nested / repeated
SELECT event_name, params.key, params.value.string_value
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_20210131`,
UNNEST(event_params) AS params
WHERE event_name = 'purchase'
LIMIT 100;

-- lab-02: window functions + CTE
WITH daily_sales AS (
  SELECT DATE(pickup_datetime) AS sale_date, SUM(total_amount) AS daily_revenue
  FROM cymbal_warehouse.taxi_trips
  GROUP BY DATE(pickup_datetime)
)
SELECT sale_date, daily_revenue,
       SUM(daily_revenue) OVER (ORDER BY sale_date) AS running_total,
       AVG(daily_revenue) OVER (ORDER BY sale_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS seven_day_avg
FROM daily_sales
ORDER BY sale_date;

-- lab-03: authorized view (dataset-level authorization required after creation)
CREATE VIEW IF NOT EXISTS cymbal_warehouse.marketing_trip_view AS
SELECT trip_id, pickup_datetime, pickup_location, dropoff_location, trip_distance, fare_amount
FROM cymbal_warehouse.taxi_trips
WHERE fare_amount > 10;

-- lab-04: UDFs
CREATE OR REPLACE FUNCTION cymbal_warehouse.normalize_currency(amount FLOAT64, from_currency STRING, to_currency STRING)
RETURNS FLOAT64 AS (
  CASE
    WHEN from_currency = 'USD' AND to_currency = 'EUR' THEN amount * 0.85
    WHEN from_currency = 'USD' AND to_currency = 'GBP' THEN amount * 0.73
    ELSE amount
  END
);

-- lab-05: materialized view
CREATE MATERIALIZED VIEW IF NOT EXISTS cymbal_warehouse.daily_trip_counts
PARTITION BY trip_date
AS
SELECT DATE(pickup_datetime) AS trip_date, vendor_id, COUNT(*) AS trip_count, SUM(fare_amount) AS total_fare
FROM cymbal_warehouse.taxi_trips
GROUP BY DATE(pickup_datetime), vendor_id;
