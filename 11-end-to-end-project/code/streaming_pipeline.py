#!/usr/bin/env python
"""Cymbal Retail streaming pipeline: Pub/Sub -> parse/enrich -> BigQuery.

Writes:
  - Bronze: clickstream_raw (every event)
  - Gold:   product_stats_streaming (fixed-window counts by product)
"""
import json
import os

import apache_beam as beam
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.trigger import AfterCount, AfterProcessingTime, AfterWatermark
from apache_beam.transforms.window import FixedWindows

PROJECT = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")
SUBSCRIPTION = f"projects/{PROJECT}/subscriptions/clickstream-sub"
RAW_TABLE = f"{PROJECT}.cymbal_warehouse.clickstream_raw"
STATS_TABLE = f"{PROJECT}.cymbal_warehouse.product_stats_streaming"

RAW_SCHEMA = (
    "event_id:STRING,user_id:STRING,session_id:STRING,timestamp:TIMESTAMP,"
    "page:STRING,product:STRING,action:STRING,value:FLOAT64,date:STRING,hour:STRING"
)


class ParseEvent(beam.DoFn):
    def process(self, element):
        event = json.loads(element.decode("utf-8"))
        ts = event["timestamp"].replace("Z", "+00:00")
        event["timestamp"] = ts
        event["date"] = ts[:10]
        event["hour"] = ts[11:13]
        yield event


def run() -> None:
    with beam.Pipeline() as p:
        events = (
            p
            | "ReadFromPubSub" >> beam.io.ReadFromPubSub(subscription=SUBSCRIPTION)
            | "ParseEvent" >> beam.ParDo(ParseEvent())
        )

        events | "WriteRaw" >> WriteToBigQuery(
            table=RAW_TABLE,
            schema=RAW_SCHEMA,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        )

        windowed = events | "Window" >> beam.WindowInto(
            FixedWindows(60),
            trigger=AfterWatermark(early=AfterProcessingTime(30), late=AfterCount(1)),
            allowed_lateness=120,
            accumulation_mode=beam.trigger.AccumulationMode.DISCARDING,
        )

        stats = (
            windowed
            | "KeyByProduct" >> beam.Map(lambda e: (e["product"], 1))
            | "CountByProduct" >> beam.CombinePerKey(sum)
            | "ToDict" >> beam.MapTuple(lambda p, c: {"product": p, "count": c})
        )

        stats | "WriteAggregated" >> WriteToBigQuery(
            table=STATS_TABLE,
            schema="product:STRING,count:INT64",
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        )


if __name__ == "__main__":
    run()
