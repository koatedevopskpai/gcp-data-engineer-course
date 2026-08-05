#!/usr/bin/env python
"""Load CSV from Cloud Storage into BigQuery."""
import os

from google.cloud import bigquery

PROJECT = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")
URI = f"gs://cymbal-raw-{PROJECT}/taxi/taxi_trips.csv"
TABLE = f"{PROJECT}.cymbal_warehouse.taxi_trips"


def main() -> None:
    client = bigquery.Client(project=PROJECT)
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )
    job = client.load_table_from_uri(URI, TABLE, job_config=job_config)
    job.result()
    table = client.get_table(TABLE)
    print(f"Loaded {table.num_rows} rows into {TABLE}")


if __name__ == "__main__":
    main()
