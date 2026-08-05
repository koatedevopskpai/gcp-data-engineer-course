from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.providers.google.cloud.operators.dataflow import DataflowStartFlexTemplateOperator

PROJECT = "gcp-data-engineering-course"

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
        project_id=PROJECT,
        location="us-central1",
        template_file_path="gs://cymbal-processed-%s/templates/wordcount.json" % PROJECT,
        parameters={
            "input": "gs://dataflow-samples/shakespeare/kinglear.txt",
            "output": "gs://cymbal-processed-%s/wordcount/out" % PROJECT,
        },
    )

    run_bigquery = BigQueryInsertJobOperator(
        task_id="run_bigquery_query",
        configuration={
            "query": {
                "query": "SELECT COUNT(*) AS n FROM `%s.cymbal_warehouse.taxi_trips`" % PROJECT,
                "useLegacySql": False,
            }
        },
    )

    start_dataflow >> run_bigquery
