#!/usr/bin/env python
"""Batch ETL: CSV from GCS -> clean -> BigQuery (see Lab 05.2)."""
import csv
import io
import os

import apache_beam as beam
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.options.pipeline_options import PipelineOptions

PROJECT = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")
INPUT = f"gs://cymbal-raw-{PROJECT}/taxi/taxi_trips.csv"
TABLE = f"{PROJECT}.cymbal_warehouse.taxi_trips_beam"
SCHEMA = (
    "trip_id:STRING,vendor_id:STRING,pickup_datetime:TIMESTAMP,"
    "fare_amount:FLOAT64,trip_distance:FLOAT64"
)


class ParseCSV(beam.DoFn):
    def process(self, element):
        for row in csv.reader(io.StringIO(element)):
            if len(row) < 5:
                continue
            yield {
                "trip_id": row[0],
                "vendor_id": row[1],
                "pickup_datetime": row[2],
                "fare_amount": float(row[3]) if row[3] else None,
                "trip_distance": float(row[4]) if row[4] else None,
            }


class CleanData(beam.DoFn):
    def process(self, element):
        if element["fare_amount"] and element["fare_amount"] > 0:
            yield element


def run() -> None:
    with beam.Pipeline() as p:
        (
            p
            | "ReadCSV" >> beam.io.ReadFromText(INPUT, skip_header_lines=1)
            | "ParseCSV" >> beam.ParDo(ParseCSV())
            | "CleanData" >> beam.ParDo(CleanData())
            | "WriteToBigQuery" >> WriteToBigQuery(
                table=TABLE,
                schema=SCHEMA,
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            )
        )


if __name__ == "__main__":
    run()
