# Lab 08.2 — DAG that Triggers Dataflow + BigQuery

## Objectives
- Write a DAG with `DataflowStartFlexTemplateOperator` and `BigQueryInsertJobOperator`.
- Upload it to the Composer DAGs folder and watch it run.

## 1. DAG (`code/dags/dataflow_etl_dag.py`)
```python
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.providers.google.cloud.operators.dataflow import DataflowStartFlexTemplateOperator

default_args = {
    "owner": "data-team",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "dataflow_etl_dag",
    default_args=default_args,
    schedule_interval="0 2 * * *",
    catchup=False,
    tags=["etl"],
) as dag:

    start_dataflow = DataflowStartFlexTemplateOperator(
        task_id="start_dataflow_job",
        project_id="gcp-data-engineering-course",
        location="us-central1",
        template_file_path="gs://cymbal-processed-gcp-data-engineering-course/templates/wordcount.json",
        parameters={
            "input": "gs://dataflow-samples/shakespeare/kinglear.txt",
            "output": "gs://cymbal-processed-gcp-data-engineering-course/wordcount/out",
        },
    )

    run_bigquery = BigQueryInsertJobOperator(
        task_id="run_bigquery_query",
        configuration={
            "query": {
                "query": "SELECT COUNT(*) AS n FROM `cymbal_warehouse.taxi_trips`",
                "useLegacySql": False,
            }
        },
    )

    start_dataflow >> run_bigquery
```

## 2. Upload + trigger
```powershell
# Copy the DAG to Composer's DAGs bucket
gsutil cp code\dags\dataflow_etl_dag.py gs://<DAG_BUCKET>/dags/

# Wait for it to appear in the Airflow UI, then trigger manually
```

## Exam notes
- Operators that "wait" on the Dataflow job: use
  `DataflowStartFlexTemplateOperator` + a follow-up — dependencies are set with `>>`.
- Airflow `catchup=False` avoids backfilling old runs by default.
