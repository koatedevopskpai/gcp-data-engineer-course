# Lab 07.4 — Streaming into Dataflow (CORRECTED)

> **Erratum:** the original course showed creating a *push* subscription whose
> endpoint was a Dataflow job URL. That is **not how Dataflow consumes Pub/Sub**.
> Dataflow reads from a **pull subscription**. Push subscriptions are for
> HTTP endpoints (Cloud Functions / Cloud Run), covered in Lab 07.3.

## Correct integration pattern
1. Create a topic (`cymbal-orders`).
2. Create a **pull subscription** (`taxi-stream-sub`).
3. Run the Dataflow streaming pipeline that pulls from it (Module 05 Lab 3).

```powershell
gcloud pubsub topics create cymbal-orders
gcloud pubsub subscriptions create taxi-stream-sub `
  --topic=cymbal-orders `
  --ack-deadline=60

python ..\05-dataflow-beam\code\streaming_taxi_pipeline.py `
  --runner=DataflowRunner --project=gcp-data-engineering-course --region=us-central1 `
  --streaming `
  --temp_location=gs://cymbal-processed-gcp-data-engineering-course/dataflow/temp
```

## How the pieces fit
```
publisher.py  ──▶  topic cymbal-orders  ──▶  subscription taxi-stream-sub  ──▶  Dataflow (pulls)
                                                                                    │
                                                            windowed aggregation → BigQuery
```

## Exam notes
- Dataflow auto-scales on Pub/Sub **backlog**.
- Set a high `ack_deadline` or streaming engine so long windows don't drop messages.
- For exactly-once end-to-end, enable exactly-once on the subscription AND use
  an idempotent sink (BigQuery dedup / primary key).
