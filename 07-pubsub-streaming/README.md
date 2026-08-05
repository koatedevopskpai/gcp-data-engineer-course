# Module 07 — Pub/Sub Streaming

Event ingestion foundation: topics, subscriptions, publishers/subscribers,
schemas, DLQ + snapshots, and integration with Dataflow.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-topic-subscription.md` | Create topic + subscription types |
| `labs/lab-02-publish.md` | Publish messages (with ordering keys) |
| `labs/lab-03-subscribe.md` | Pull/push subscribers + exactly-once |
| `labs/lab-04-streaming-dataflow.md` | Stream Pub/Sub → Dataflow |
| `labs/lab-05-dlq-seek-snapshot.md` | Dead-letter topics, seek, snapshots |
| `code/publisher.py` | Publisher (verified: 100 msgs, ordering) |
| `code/subscriber.py` | Subscriber (pull + ack) |
| `code/dlq_processor.py` | Dead-letter reprocessing script |
| `code/order.avsc` | Avro message schema |
| `code/push_subscriber_function/` | Cloud Function push subscriber |
| `exercises/exercises.md` | Self-check questions |

## Verified gotchas

- **Ordering keys require message ordering to be enabled on the client**:
  the publisher must pass `PublisherOptions(enable_message_ordering=True)`,
  otherwise publishing an ordered message raises a client-side `ValueError`.
- `PublisherClient` has no `close()`; call `stop()` to release resources.
- Subscription must be created with `--enable-message-ordering
  --enable-exactly-once-delivery` to match the ordered, exactly-once pipeline.
- Dataflow **pulls** from a subscription — the original draft's "push
  subscription to Dataflow" was incorrect (see COURSE-MASTER errata).

## Exam notes

- Delivery models: **pull** (subscriber pulls, then ack) vs **push**
  (Pub/Sub POSTs to a HTTPS endpoint); **exactly-once** delivery is a
  subscription option.
- **Ordering** (message ordering key) guarantees per-key ordering; DLQ topics
  capture undeliverable messages; **snapshots/seek** enable replay.
- `attributes` (key/value metadata) vs `data` (payload); schemas validate
  messages (Avro/Proto).
