# Lab 06.5 — Dataproc Workflow Templates

## Objectives
- Define a workflow template that creates a managed cluster and runs multiple jobs.
- Instantiate the template.

## Steps

```powershell
# 1. Create the template
gcloud dataproc workflow-templates create taxi-workflow --region=us-central1

# 2. Configure a managed cluster (auto-created for the workflow)
gcloud dataproc workflow-templates set-managed-cluster taxi-workflow `
  --region=us-central1 `
  --cluster-name=taxi-cluster `
  --master-machine-type=n1-standard-2 `
  --worker-machine-type=n1-standard-2 `
  --num-workers=2 `
  --num-preemptible-workers=2

# 3. Add jobs in order
gcloud dataproc workflow-templates add-job pyspark taxi-workflow `
  --step-id=analysis-step `
  --pyspark-file=gs://cymbal-processed-<PROJECT>/scripts/taxi_analysis.py `
  --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar

gcloud dataproc workflow-templates add-job spark-sql taxi-workflow `
  --step-id=sql-step `
  --sql-file=gs://cymbal-processed-<PROJECT>/scripts/taxi_analysis.sql

# 4. Upload scripts to GCS first
gsutil cp code/taxi_analysis.py code/taxi_analysis.sql gs://cymbal-processed-<PROJECT>/scripts/

# 5. Instantiate (creates cluster, runs jobs, deletes cluster)
gcloud dataproc workflow-templates instantiate taxi-workflow --region=us-central1
```

## Exam notes
- Workflow templates = **scheduled/orchestrated multi-job Dataproc** without a
  permanently running cluster → lower cost.
- The managed cluster is created for the run and deleted automatically.
- Cloud Composer can call `instantiate` for day-level orchestration.
