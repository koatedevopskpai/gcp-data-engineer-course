# Lab 05.4 — Side Inputs (Enrichment)

## Objectives
- Attach a static lookup table to a ParDo/Map.
- Enrich streaming/batch records with reference data.

## Pipeline (`code/side_input_pipeline.py`)
```python
lookup = p | "CreateLookup" >> beam.Create(
    [("P001", {"category": "Electronics", "price": 100.0}),
     ("P002", {"category": "Books", "price": 20.0})]
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
```

## Side-input patterns
| Pattern | Use |
|---|---|
| `AsDict` | key→value lookup (most common) |
| `AsList` | iterate a full list |
| `AsSingleton` | single value / config |
| `AsIter` | stream a PCollection (avoid materializing) |

## Exam notes
- Side inputs are read once and **broadcast**; they do NOT change per element.
- Use them for reference data that fits in memory; join for huge reference sets.
- Side inputs in streaming: a side input PCollection is a global-window snapshot
  (re-evaluated per window of the main input only in bounded fashion).
