# Module 06 — Dataproc & Apache Spark

Managed Spark on GCP: PySpark, Spark SQL, the BigQuery connector, and
Dataproc workflow templates.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-create-cluster.md` | Create/scale/delete a Dataproc cluster |
| `labs/lab-02-pyspark.md` | Run PySpark jobs |
| `labs/lab-03-spark-sql.md` | Spark SQL via `spark-sql` |
| `labs/lab-04-bigquery-connector.md` | Read/write BigQuery from Spark |
| `labs/lab-05-workflow-template.md` | Orchestrate jobs with workflow templates |
| `code/bigquery_spark_pipeline.py` | PySpark ETL reading GCS → BigQuery |
| `code/taxi_analysis.py` | PySpark analysis of `taxi_trips.csv` |
| `code/taxi_analysis.sql` | Equivalent Spark SQL |
| `exercises/exercises.md` | Self-check questions |

## TL;DR

```bash
gcloud dataproc clusters create cymbal-cluster \
  --region=us-central1 --single-node \
  --preemptible-worker-boot-disk-size=30GB \
  --image-version=2.2-debian12

gcloud dataproc jobs submit pyspark code/taxi_analysis.py --cluster=cymbal-cluster --region=us-central1
gcloud dataproc clusters delete cymbal-cluster --region=us-central1
```

All code reads `PROJECT_ID` from the environment (default
`gcp-data-engineering-course`) so it works on any project.

## Exam notes

- Dataproc = managed Spark/Hadoop; ephemeral clusters + preemptible workers
  keep cost low — **always delete the cluster after the lab**.
- The **BigQuery connector** (spark-bigquery) lets Spark read/write BQ tables
  without GCS intermediate files.
- Workflow templates = DAG of Dataproc jobs; `gcloud dataproc
  workflows create/submit` (vs Composer's full Airflow for complex DAGs).
