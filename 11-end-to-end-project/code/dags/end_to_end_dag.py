"""Hourly Composer DAG: validate incoming data, refresh marts, alert on failure.

Run prerequisites:
  - Composer environment (Module 08) with `dbt-bigquery` installed (custom
    Composer image or `pip install dbt-bigquery` on the environment).
  - The dbt project synced into the environment's dags folder:
    `gsutil cp -r ../../dbt gs://<env-bucket>/dags/dbt`
  - Set the Airflow variable `dbt_project_dir` (or env DBT_PROJECT_DIR) to the
    dbt project location; default is /home/airflow/gcs/dags/dbt.
"""
import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

PROJECT = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")
DBT_PROJECT_DIR = Variable.get(
    "dbt_project_dir",
    default_var=os.environ.get("DBT_PROJECT_DIR", "/home/airflow/gcs/dags/dbt"),
)

default_args = {
    "owner": "data-team",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


def send_alert(**_):
    # Replace with Slack/email/Pub/Sub in production.
    print("Alert: hourly Cymbal refresh completed or failed.")


with DAG(
    "cymbal_hourly_refresh",
    default_args=default_args,
    schedule_interval="0 * * * *",
    catchup=False,
    tags=["cymbal"],
) as dag:

    validate = BigQueryInsertJobOperator(
        task_id="validate_raw",
        configuration={
            "query": {
                "query": f"""
                    SELECT COUNT(*) AS n
                    FROM `{PROJECT}.cymbal_warehouse.clickstream_raw`
                    WHERE date = FORMAT_DATE('%Y-%m-%d', CURRENT_DATE())
                """,
                "useLegacySql": False,
            }
        },
    )

    run_dbt = BashOperator(
        task_id="run_dbt_marts",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run --target prod",
    )

    alert = PythonOperator(
        task_id="send_alert",
        python_callable=send_alert,
        trigger_rule="all_done",
    )

    validate >> run_dbt >> alert
