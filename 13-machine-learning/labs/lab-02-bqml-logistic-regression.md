# Lab 13.2 — BigQuery ML: Logistic Regression (Churn)

## Objectives
- Train a classifier on a churn feature set.
- Use `ML.ROC_CURVE` / `ML.CONFUSION_MATRIX` to evaluate.

## 1. Build a churn label + train
```sql
-- Assume cymbal_warehouse.customers has churn-related features.
CREATE OR REPLACE MODEL cymbal_warehouse.churn_model
OPTIONS (
  model_type = 'LOGISTIC_REG',
  input_label_cols = ['is_churn'],
  auto_class_weights = TRUE
) AS
SELECT
  tenure_months,
  orders_last_90d,
  avg_order_value,
  support_calls,
  is_churn
FROM cymbal_warehouse.customers;
```

## 2. Evaluate
```sql
SELECT *
FROM ML.EVALUATE(MODEL cymbal_warehouse.churn_model);
```

```sql
SELECT *
FROM ML.ROC_CURVE(MODEL cymbal_warehouse.churn_model);
```

```sql
SELECT *
FROM ML.CONFUSION_MATRIX(MODEL cymbal_warehouse.churn_model,
  (SELECT tenure_months, orders_last_90d, avg_order_value, support_calls, is_churn
   FROM cymbal_warehouse.customers WHERE is_churn IS NOT NULL));
```

## 3. Predict probabilities
```sql
SELECT *
FROM ML.PREDICT(MODEL cymbal_warehouse.churn_model,
  (SELECT tenure_months, orders_last_90d, avg_order_value, support_calls
   FROM cymbal_warehouse.customers));
-- predicted_is_churn + predicted_is_churn_probs[0].prob
```

## Exam notes
- Logistic regression = binary classification → outputs probabilities.
- `auto_class_weights` helps imbalanced labels.
- Know `ML.ROC_CURVE`, `ML.CONFUSION_MATRIX`, `ML.EVALUATE`, `ML.PREDICT`.
