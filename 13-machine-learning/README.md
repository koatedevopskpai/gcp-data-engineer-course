# Module 13 — Machine Learning on GCP

ML on the data platform: BigQuery ML (BQML) for in-warehouse modeling and
Vertex AI for production model serving, training, and monitoring.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-bqml-linear-regression.md` | `CREATE MODEL` + linear regression |
| `labs/lab-02-bqml-logistic-regression.md` | Classification with BQML |
| `labs/lab-03-bqml-clustering-forecast.md` | Clustering + time-series forecasting |
| `labs/lab-04-vertex-ai.md` | Vertex AI: datasets, training, endpoints |
| `labs/lab-05-lifecycle-monitoring.md` | ML lifecycle + monitoring |
| `code/bqml.sql` | All BQML statements in one runnable file |
| `code/vertex_batch.py` | Vertex AI batch-prediction script |
| `exercises/exercises.md` | Self-check questions |

## TL;DR (BQML)

```sql
CREATE OR REPLACE MODEL `cymbal_warehouse.taxi_fare_model`
OPTIONS(model_type='LINEAR_REG', input_label_cols=['fare_amount'])
AS SELECT * FROM `cymbal_warehouse.taxi_trips_ml`;

SELECT * FROM ML.PREDICT(MODEL `cymbal_warehouse.taxi_fare_model`,
  (SELECT * FROM `cymbal_warehouse.taxi_trips_test`));
```

## Exam notes

- **BQML** runs ML inside BigQuery (no data egress): regression/classification,
  clustering (`KMEANS`), forecasting (`ARIMA_PLUS`), and Vertex AI integration
  (`ML.EXPORT_MODEL`, `model_type='XGBOOST'`, `BOOSTED_TREE_CLASSIFIER`).
- **Vertex AI** = unified ML platform (Vertex AI Pipelines, Training, Endpoints,
  Prediction, Model Registry); batch prediction scales without serving VMs.
- Model lifecycle: data → training → evaluation → deployment → **monitoring**
  (drift/skew) → retraining. AutoML for code-free modeling.
- Costs: BQML bills BigQuery slots; Vertex endpoints bill per VM hour —
  delete endpoints after labs.
