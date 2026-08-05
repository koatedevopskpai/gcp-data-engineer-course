# Lab 13.1 — BigQuery ML: Linear Regression (Fare Prediction)

## Objectives
- Train a linear regression model in BigQuery (no data movement).
- Evaluate with `ML.EVALUATE`, predict with `ML.PREDICT`.

## 1. Train
```sql
CREATE OR REPLACE MODEL cymbal_warehouse.fare_model
OPTIONS (
  model_type = 'LINEAR_REG',
  input_label_cols = ['fare_amount'],
  data_split_method = 'AUTO_SPLIT'
) AS
SELECT
  trip_distance,
  passenger_count,
  vendor_id,
  TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, MINUTE) AS duration_min,
  fare_amount
FROM cymbal_warehouse.taxi_trips
WHERE fare_amount > 0
  AND trip_distance > 0;
```

## 2. Evaluate
```sql
SELECT *
FROM ML.EVALUATE(MODEL cymbal_warehouse.fare_model);
-- look at: mean_absolute_error, r2_score, root_mean_squared_error
```

## 3. Predict
```sql
SELECT
  predicted_fare_amount,
  fare_amount AS actual
FROM ML.PREDICT(MODEL cymbal_warehouse.fare_model,
  (SELECT trip_distance, passenger_count, vendor_id,
          TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, MINUTE) AS duration_min
   FROM cymbal_warehouse.taxi_trips
   WHERE fare_amount > 0 LIMIT 100));
```

## 4. Explain (feature contributions)
```sql
SELECT *
FROM ML.EXPLAIN_PREDICT(MODEL cymbal_warehouse.fare_model,
  (SELECT trip_distance, passenger_count, vendor_id,
          TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, MINUTE) AS duration_min
   FROM cymbal_warehouse.taxi_trips LIMIT 10));
```

## Exam notes
- BQML trains **inside BigQuery** — no data egress; SQL-first.
- `input_label_cols` names the label; `model_type` selects the algorithm.
- Support: LINEAR_REG, LOGISTIC_REG, BOOSTED_TREE_*, RANDOM_FOREST, KMEANS,
  ARIMA_PLUS (forecasting), MATRIX_FACTORIZATION (recommendations), DNN.
