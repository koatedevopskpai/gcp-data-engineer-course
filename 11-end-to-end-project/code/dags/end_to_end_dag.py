"""Hourly Composer DAG: validate incoming data, refresh marts, alert on failure."""
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

PROJECT = "gcp-data-engineering-course"

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
        bash_command="cd /home/airflow/gcs/dags/dbt && dbt run --target prod",
    )

    alert = PythonOperator(
        task_id="send_alert",
        python_callable=send_alert,
        trigger_rule="all_done",
    )

    validate >> run_dbt >> alert
