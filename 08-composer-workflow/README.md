# Module 08 — Cloud Composer & Workflows

Orchestration: Airflow DAGs on Cloud Composer, plus the lighter-weight Cloud
Workflows alternative, and monitoring/alerting.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-create-composer.md` | Create a Composer environment (auto-scaling) |
| `labs/lab-02-dag-dataflow.md` | Trigger Dataflow from an Airflow DAG |
| `labs/lab-03-bigquery-schedule.md` | Schedule BigQuery SQL |
| `labs/lab-04-workflows.md` | Cloud Workflows YAML (serverless orchestration) |
| `labs/lab-05-monitor.md` | Monitoring + alerting policy |
| `code/dags/dataflow_etl_dag.py` | DAG triggering the Beam ETL |
| `code/dags/bigquery_schedule_dag.py` | DAG running BigQuery queries |
| `code/workflows/etl_workflow.yaml` | Cloud Workflows orchestration |
| `code/alerting-policy.json` | Alerting policy (validated) |
| `exercises/exercises.md` | Self-check questions |

## Exam notes

- **Composer = managed Airflow**: DAGs live in the environment's GCS bucket
  (`dags/`); trigger via `DataflowStartFlexTemplateOperator`,
  `BigQueryInsertJobOperator`, etc.
- Read the project from `os.environ.get("PROJECT_ID")` / Airflow variables so
  DAGs are portable across projects.
- **Cloud Workflows** is a serverless alternative to full Airflow for simple
  step orchestration (JSON/YAML steps, HTTP calls, BigQuery jobs).
- Alerting: `composer.googleapis.com/workflow/run_count` with
  `status == "failed"` (the alerting policy JSON is validated).

**Cost warning:** Composer environments are expensive — delete
(`gcloud composer environments delete`) as soon as a lab is done.
