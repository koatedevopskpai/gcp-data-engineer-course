#!/usr/bin/env python
"""Side inputs: enrich orders with a static lookup table (see Lab 05.4)."""
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run() -> None:
    options = PipelineOptions()
    with beam.Pipeline(options=options) as p:
        lookup = (
            p
            | "CreateLookup" >> beam.Create(
                [
                    ("P001", {"category": "Electronics", "price": 100.0}),
                    ("P002", {"category": "Books", "price": 20.0}),
                ]
            )
        )
        lookup_dict = lookup | "ToDict" >> beam.combiners.ToDict()

        orders = p | "CreateOrders" >> beam.Create(
            [("P001", 3), ("P002", 1), ("P999", 5)]
        )

        enriched = orders | "Enrich" >> beam.MapTuple(
            lambda product_id, qty, lookup: {
                "product_id": product_id,
                "quantity": qty,
                "category": lookup.get(product_id, {}).get("category", "Unknown"),
                "line_total": lookup.get(product_id, {}).get("price", 0.0) * qty,
            },
            lookup=beam.pvalue.AsDict(lookup_dict),
        )

        enriched | "Print" >> beam.Map(print)


if __name__ == "__main__":
    run()
