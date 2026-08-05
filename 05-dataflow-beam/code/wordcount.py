#!/usr/bin/env python
"""WordCount example for Apache Beam (DirectRunner or DataflowRunner)."""
import argparse

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run(argv=None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="gs://dataflow-samples/shakespeare/kinglear.txt")
    parser.add_argument("--output", default="wordcount_output")
    known, pipeline_args = parser.parse_known_args(argv)

    with beam.Pipeline(options=PipelineOptions(pipeline_args)) as p:
        (
            p
            | "Read" >> beam.io.ReadFromText(known.input)
            | "Split" >> beam.FlatMap(lambda line: line.split())
            | "FilterEmpty" >> beam.Filter(lambda word: len(word.strip()) > 0)
            | "Count" >> beam.combiners.Count.PerElement()
            | "Format" >> beam.Map(lambda kv: f"{kv[0]}: {kv[1]}")
            | "Write" >> beam.io.WriteToText(known.output)
        )


if __name__ == "__main__":
    run()
