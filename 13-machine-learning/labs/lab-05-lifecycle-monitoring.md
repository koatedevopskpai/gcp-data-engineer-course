# Lab 13.5 — Model Lifecycle, Monitoring & Cost

## Objectives
- Version models in the Vertex AI Model Registry.
- Monitor drift with Vertex AI Model Monitoring.
- Keep ML cost under control.

## 1. Model Registry / versioning
- Upload each retrain with a new version (`gcloud ai models upload --version-alias=v2`).
- Serve traffic: split or migrate between versions on an endpoint.

## 2. Monitoring
- Vertex AI **Model Monitoring**: skew (training vs serving) and drift detection
  on features; alerts via email/Cloud Monitoring.
- BigQuery: monitor BQML training jobs via `INFORMATION_SCHEMA.MODELS`:
  ```sql
  SELECT model_name, creation_time, last_modified_time
  FROM `region-us-central1`.INFORMATION_SCHEMA.MODELS
  ORDER BY creation_time DESC;
  ```

## 3. Cost control
- Delete endpoints after labs.
- Use batch prediction instead of online endpoints for large offline jobs.
- Prefer **BQML** when data is already in BigQuery (no transfer, free tier applies).
- Training in Vertex AI: use `n1-standard` small machines; stop jobs.

## Exam notes
- The 15–20% ML domain tests **operationalizing** models: versioning, monitoring,
  batch vs online serving, and feature engineering — not deep ML math.
- **Vertex AI Pipelines** (Kubeflow) for CI/CD of models is exam-relevant.
