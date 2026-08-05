# Lab 07.5 — Dead Letter Queues, Snapshots & Seek

## Objectives
- Configure a dead-letter topic on a subscription.
- Process DLQ messages.
- Replay messages with snapshots and seek.

## 1. DLQ setup
```powershell
gcloud pubsub topics create cymbal-orders-dlq

# Subscription that moves failed messages to the DLQ after 5 attempts
gcloud pubsub subscriptions create cymbal-orders-sub-dlq `
  --topic=cymbal-orders `
  --dead-letter-topic=cymbal-orders-dlq `
  --max-delivery-attempts=5 `
  --ack-deadline=60

# A subscriber just for the DLQ
gcloud pubsub subscriptions create cymbal-orders-dlq-sub --topic=cymbal-orders-dlq
```

## 2. DLQ processor (`code/dlq_processor.py`)
```python
from google.cloud import pubsub_v1
import json

def process_dlq(message):
    data = json.loads(message.data.decode("utf-8"))
    print(f"DLQ: {data['order_id']} attempt={message.delivery_attempt}")
    message.ack()

sub = pubsub_v1.SubscriberClient()
path = sub.subscription_path("gcp-data-engineering-course", "cymbal-orders-dlq-sub")
sub.subscribe(path, callback=process_dlq).result()
```

## 3. Snapshot + seek (replay)
```powershell
# Snapshot the subscription state
gcloud pubsub snapshots create orders-snapshot --subscription=cymbal-orders-sub

# Seek back to the snapshot (replay)
gcloud pubsub subscriptions seek cymbal-orders-sub --snapshot=orders-snapshot

# Or seek to a point in time
gcloud pubsub subscriptions seek cymbal-orders-sub --time=2024-01-01T00:00:00Z
```

## Exam notes
- DLQ: after N delivery attempts a message moves to the DLQ topic; set
  `--max-delivery-attempts`.
- **Seek** resets a subscription's offset; **snapshots** let you restore later.
- Snapshots require the subscription to be in the same project & region.
