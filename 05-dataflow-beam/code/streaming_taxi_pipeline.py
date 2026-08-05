#!/usr/bin/env python
"""Streaming pipeline: Pub/Sub (pull) -> fixed windows + triggers -> BigQuery.

CORRECTED: reads from a Pub/Sub *subscription* (Dataflow pulls). There is no
push subscription to Dataflow.
"""
import json
import os

import apache_beam as beam
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.trigger import AfterCount, AfterProcessingTime, AfterWatermark
from apache_beam.transforms.window import FixedWindows

PROJECT = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")
SUBSCRIPTION = f"projects/{PROJECT}/subscriptions/taxi-stream-sub"
TABLE = f"{PROJECT}.cymbal_warehouse.vendor_stats_streaming"


class ParseMessage(beam.DoFn):
    def process(self, element):
        payload = element.data if hasattr(element, "data") else element
        if isinstance(payload, (bytes, bytearray)):
            payload = payload.decode("utf-8")
        data = json.loads(payload)
        yield {
            "vendor_id": data.get("vendor_id"),
            "total_amount": float(data.get("total_amount", 0.0)),
        }


def run() -> None:
    options = PipelineOptions()
    with beam.Pipeline(options=options) as p:
        parsed = (
            p
            | "ReadFromPubSub" >> beam.io.ReadFromPubSub(
                subscription=SUBSCRIPTION, with_attributes=True
            )
            | "Parse" >> beam.ParDo(ParseMessage())
        )

        windowed = parsed | "Window" >> beam.WindowInto(
            FixedWindows(60),
            trigger=AfterWatermark(
                early=AfterProcessingTime(30),
                late=AfterCount(1),
            ),
            allowed_lateness=120,
            accumulation_mode=beam.trigger.AccumulationMode.ACCUMULATING,
        )

        stats = (
            windowed
            | "KeyByVendor" >> beam.Map(lambda x: (x["vendor_id"], x["total_amount"]))
            | "SumByVendor" >> beam.CombinePerKey(sum)
            | "ToDict" >> beam.MapTuple(lambda k, v: {"vendor_id": k, "total_amount": v})
        )

        stats | "WriteToBigQuery" >> WriteToBigQuery(
            table=TABLE,
            schema="vendor_id:STRING,total_amount:FLOAT64",
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        )


if __name__ == "__main__":
    run()
