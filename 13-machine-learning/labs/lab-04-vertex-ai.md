# Lab 13.4 — Vertex AI: Training, Endpoint, Batch Prediction

## Objectives
- Create a Vertex AI dataset and train a model.
- Deploy to an online endpoint, run batch prediction.
- Delete everything after (cost!).

## 1. Enable + prep
```powershell
gcloud services enable aiplatform.googleapis.com
gcloud ai models list --region=us-central1
```

## 2. Batch prediction via BQML→Vertex, or a managed model
You can import a BigQuery ML model into Vertex AI:
```powershell
gcloud ai models upload `
  --region=us-central1 `
  --display-name=fare_model `
  --artifact-uri=gs://cymbal-processed-gcp-data-engineering-course/models/fare_model `
  --container-image-uri=us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-12:latest
```

Or create a batch prediction job on an AutoML/tabular model via the console:
1. Vertex AI → Datasets → create (BigQuery source).
2. Train → AutoML tabular / custom training.
3. Deploy to **endpoint** (online) OR **batch prediction** (offline, cheaper).

## 3. Python client (`code/vertex_batch.py`)
```python
from google.cloud import aiplatform

aiplatform.init(project="gcp-data-engineering-course", location="us-central1")

# Batch prediction on a deployed model
model = aiplatform.Model("projects/gcp-data-engineering-course/locations/us-central1/models/MODEL_ID")
batch_job = model.batch_predict(
    job_display_name="fare_batch",
    gcs_source="gs://cymbal-raw-<PROJECT>/predictions/input.jsonl",
    gcs_destination_prefix="gs://cymbal-processed-<PROJECT>/predictions/",
    machine_type="n1-standard-2",
)
batch_job.wait()
```

## 4. ALWAYS clean up
```powershell
gcloud ai endpoints delete ENDPOINT_ID --region=us-central1
gcloud ai models delete MODEL_ID --region=us-central1
```

## Exam notes
- **Vertex AI** = unified MLOps (datasets, training, endpoints, batch, Feature
  Store, Pipelines, Model Registry).
- **Online endpoint** = low-latency serving (auto-scaling, cost per instance).
- **Batch prediction** = offline, cheaper, for large volumes.
- Decision: **BQML** (in-warehouse, SQL) vs **Vertex AI** (custom/deep learning,
  full MLOps) vs **Dataproc MLlib** (huge custom feature engineering).
