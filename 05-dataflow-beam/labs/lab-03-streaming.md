# Lab 05.3 — Batch → Streaming: Pub/Sub to BigQuery (CORRECTED)

> **Erratum:** Dataflow does **not** receive Pub/Sub messages via a *push*
> subscription. A Dataflow streaming pipeline **pulls** from a Pub/Sub subscription.
> Push subscriptions are for HTTP endpoints such as Cloud Functions/Cloud Run
> (see Module 07 Lab 4).

## Objectives
- Convert a batch pipeline into a streaming pipeline.
- Read from a Pub/Sub subscription (pull).
- Apply fixed windows + triggers + `allowed_lateness` for late data.
- Write aggregated results to BigQuery.

## 1. Create the subscription first
```powershell
gcloud pubsub topics create cymbal-orders
gcloud pubsub subscriptions create taxi-stream-sub `
  --topic=cymbal-orders `
  --ack-deadline=60
```

## 2. Streaming pipeline (`code/streaming_taxi_pipeline.py`)
```python
with beam.Pipeline(options=options) as p:
    msgs = p | "ReadFromPubSub" >> beam.io.ReadFromPubSub(
        subscription="projects/{PROJECT}/subscriptions/taxi-stream-sub",
        with_attributes=True,
    )
    parsed = msgs | "Parse" >> beam.ParDo(ParseMessage())

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

    stats | "WriteToBQ" >> WriteToBigQuery(
        table="{PROJECT}.cymbal_warehouse.vendor_stats_streaming",
        schema="vendor_id:STRING,total_amount:FLOAT64",
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
    )
```

## 3. Run + publish test data
```powershell
python code\streaming_taxi_pipeline.py `
  --runner=DataflowRunner --project=gcp-data-engineering-course --region=us-central1 `
  --streaming `
  --temp_location=gs://cymbal-processed-gcp-data-engineering-course/dataflow/temp `
  --max_num_workers=2

# In another terminal, publish messages:
python code\..\..\07-pubsub-streaming\code\publisher.py
```

## 4. Stop the job when done
```powershell
gcloud dataflow jobs list --region=us-central1 --filter="state:JOB_STATE_RUNNING"
gcloud dataflow jobs cancel <JOB_ID> --region=us-central1
```

## Windowing & triggers (exam-critical)
- **Watermark**: BigQuery/Dataflow estimate that all data up to time T arrived.
- **Early/on-time/late**: triggers fire before watermark (early), at watermark
  (on-time), and after watermark (late) within `allowed_lateness`.
- **ACCUMULATING** re-emits updated totals; **DISCARDING** emits only deltas.
- Windows: **fixed** (tumbling), **sliding** (overlap), **session** (gap-based),
  **global** (batch default).
- Exactly-once semantics require idempotent sinks (BigQuery supports dedup by
  primary key on streaming inserts).
