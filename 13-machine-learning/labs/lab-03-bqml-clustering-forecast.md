# Lab 13.3 — BigQuery ML: K-Means Clustering + Forecasting

## Objectives
- Segment customers with unsupervised k-means.
- Forecast with ARIMA_PLUS.

## 1. K-means customer segmentation
```sql
CREATE OR REPLACE MODEL cymbal_warehouse.customer_segments
OPTIONS (
  model_type = 'KMEANS',
  num_clusters = 4,
  standardize_features = TRUE
) AS
SELECT
  avg_order_value,
  orders_last_90d,
  total_revenue,
  region
FROM cymbal_warehouse.customers;
```
```sql
-- Assign clusters to rows
SELECT *
FROM ML.PREDICT(MODEL cymbal_warehouse.customer_segments,
  (SELECT * FROM cymbal_warehouse.customers))
LIMIT 10;
```
```sql
-- Centroid means per cluster (for profiling)
SELECT centroid_id, feature, AVG(numerical_value) AS mean
FROM ML.CENTROIDS(MODEL cymbal_warehouse.customer_segments)
GROUP BY centroid_id, feature
ORDER BY centroid_id, feature;
```

## 2. ARIMA_PLUS time-series forecast
```sql
CREATE OR REPLACE MODEL cymbal_warehouse.sales_forecast
OPTIONS (model_type = 'ARIMA_PLUS',
         time_series_timestamp_col = 'day',
         time_series_data_col = 'daily_revenue') AS
SELECT day, daily_revenue FROM cymbal_warehouse.daily_sales;
```
```sql
SELECT *
FROM ML.FORECAST(MODEL cymbal_warehouse.sales_forecast,
                 STRUCT(30 AS horizon, 0.95 AS confidence_level));
```

## Exam notes
- `ML.FORECAST` horizon = number of future periods.
- ARIMA_PLUS handles seasonality, holidays, and trend automatically.
- K-means: `num_clusters`, `standardize_features`; centroid interpretation is a
  classic exam question.
