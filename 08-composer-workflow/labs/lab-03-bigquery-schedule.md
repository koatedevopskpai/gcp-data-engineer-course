# Lab 08.3 — Scheduled BigQuery Report DAG

## Objectives
- Create a daily-report DAG that materializes a summary table.

## DAG (`code/dags/bigquery_schedule_dag.py`)
```python
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

default_args = {
    "owner": "data-team",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    "daily_report_dag",
    default_args=default_args,
    schedule_interval="0 6 * * *",
    catchup=False,
    tags=["reporting"],
) as dag:

    generate_report = BigQueryInsertJobOperator(
        task_id="generate_daily_report",
        configuration={
            "query": {
                "query": """
                    CREATE OR REPLACE TABLE `cymbal_warehouse.daily_sales_report`
                    PARTITION BY report_date
                    AS
                    SELECT
                      DATE(pickup_datetime) AS report_date,
                      vendor_id,
                      COUNT(*)             AS trip_count,
                      SUM(fare_amount)     AS total_revenue,
                      AVG(fare_amount)     AS avg_fare
                    FROM `cymbal_warehouse.taxi_trips`
                    WHERE DATE(pickup_datetime) = CURRENT_DATE() - 1
                    GROUP BY report_date, vendor_id
                """,
                "useLegacySql": False,
            }
        },
    )

    generate_report
```

## Exam notes
- `BigQueryInsertJobOperator` runs a query (DDL or DML) — a common Composer task.
- `CURRENT_DATE() - 1` makes the DAG **idempotent** for daily runs.
