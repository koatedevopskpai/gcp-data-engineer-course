#!/usr/bin/env python
"""Parameterized Flex Template pipeline (see Lab 05.5)."""
import argparse

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run(argv=None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="GCS input path")
    parser.add_argument("--output", required=True, help="GCS output prefix")
    known, pipeline_args = parser.parse_known_args(argv)

    with beam.Pipeline(options=PipelineOptions(pipeline_args)) as p:
        (
            p
            | "Read" >> beam.io.ReadFromText(known.input)
            | "Split" >> beam.FlatMap(lambda x: x.split())
            | "Count" >> beam.combiners.Count.PerElement()
            | "Format" >> beam.Map(lambda kv: f"{kv[0]}: {kv[1]}")
            | "Write" >> beam.io.WriteToText(known.output)
        )


if __name__ == "__main__":
    run()
