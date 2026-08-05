-- BigQuery ML scripts (Module 13)

-- Lab 13.1: Linear regression
CREATE OR REPLACE MODEL cymbal_warehouse.fare_model
OPTIONS (model_type = 'LINEAR_REG', input_label_cols = ['fare_amount']) AS
SELECT
  trip_distance,
  passenger_count,
  vendor_id,
  TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, MINUTE) AS duration_min,
  fare_amount
FROM cymbal_warehouse.taxi_trips
WHERE fare_amount > 0 AND trip_distance > 0;

SELECT * FROM ML.EVALUATE(MODEL cymbal_warehouse.fare_model);

SELECT predicted_fare_amount, fare_amount AS actual
FROM ML.PREDICT(MODEL cymbal_warehouse.fare_model,
  (SELECT trip_distance, passenger_count, vendor_id,
          TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, MINUTE) AS duration_min
   FROM cymbal_warehouse.taxi_trips WHERE fare_amount > 0 LIMIT 100));

-- Lab 13.3: K-means
CREATE OR REPLACE MODEL cymbal_warehouse.customer_segments
OPTIONS (model_type = 'KMEANS', num_clusters = 4, standardize_features = TRUE) AS
SELECT avg_order_value, orders_last_90d, total_revenue, region
FROM cymbal_warehouse.customers;

-- Lab 13.3: Forecasting
CREATE OR REPLACE MODEL cymbal_warehouse.sales_forecast
OPTIONS (model_type = 'ARIMA_PLUS',
         time_series_timestamp_col = 'day',
         time_series_data_col = 'daily_revenue') AS
SELECT day, daily_revenue FROM cymbal_warehouse.daily_sales;

SELECT *
FROM ML.FORECAST(MODEL cymbal_warehouse.sales_forecast,
                 STRUCT(30 AS horizon, 0.95 AS confidence_level));
