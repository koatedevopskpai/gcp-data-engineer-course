# Lab 08.1 — Cloud Composer Environment (with cost warning)

> **COST WARNING:** a Composer-2 environment costs roughly $1–3/day. Create it,
> run the labs, and **delete it the same day** to stay inside the free credits.
> For DAG development, prefer local Airflow (Docker/`astro`) — see below.

## Steps
```powershell
gcloud composer environments create data-pipeline-env `
  --location=us-central1 `
  --image-version=composer-2.6.2-airflow-2.7.2 `
  --machine-type=n1-standard-2 `
  --node-count=3 `
  --environment-size=small

# Get the Airflow web UI URL
gcloud composer environments describe data-pipeline-env `
  --location=us-central1 --format="value(config.airflowUri)"

# Find the DAGs GCS folder
gcloud composer environments describe data-pipeline-env `
  --location=us-central1 --format="value(config.dagGcsPrefix)"
```

## Local Airflow for DAG development (free)
```powershell
# Option: use the astronomer CLI (astro) with a local Docker Airflow
docker run --rm -d -p 8080:8080 `
  -e AIRFLOW__CORE__LOAD_EXAMPLES=False `
  apache/airflow:2.7.2 standalone
```

## ALWAYS clean up
```powershell
gcloud composer environments delete data-pipeline-env --location=us-central1
```

## Exam notes
- Composer is **managed Airflow**; exam cares about DAG structure, operators,
  dependencies, and when to use it vs Cloud Workflows vs Cloud Scheduler.
