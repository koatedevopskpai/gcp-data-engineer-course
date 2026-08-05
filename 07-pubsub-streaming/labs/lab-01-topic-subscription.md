# Lab 07.1 — Topics, Subscriptions & Schema Registry

## Objectives
- Create a topic and a pull subscription with ordering + exactly-once.
- Create a Pub/Sub schema (Avro) and attach it to a topic.

## 1. Topic + subscription
```powershell
gcloud pubsub topics create cymbal-orders --message-retention-duration=7d

# Pull subscription with ordering + exactly-once
gcloud pubsub subscriptions create cymbal-orders-sub `
  --topic=cymbal-orders `
  --ack-deadline=60 `
  --enable-message-ordering `
  --enable-exactly-once-delivery
```

## 2. Schema registry
```powershell
# Create Avro schema (see code/order.avsc)
gcloud pubsub schemas create order-schema --type=AVRO --definition-file=code\order.avsc

# Attach to a new topic
gcloud pubsub topics create cymbal-orders-schema `
  --schema=order-schema `
  --message-encoding=JSON
```

## 3. List / describe
```powershell
gcloud pubsub topics list
gcloud pubsub subscriptions list
gcloud pubsub schemas describe order-schema
```

## Exam notes
- **Exactly-once delivery** (subscription-level) prevents duplicates **within the
  subscriber** within a retention window; still make sinks idempotent.
- **Ordering keys** give per-key ordering, NOT global FIFO.
- **Schema registry** validates message structure at publish → data quality at
  the ingestion layer (Avro/Protobuf).
