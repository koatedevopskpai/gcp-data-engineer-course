# Lab 07.3 — Subscribe and Process (Pull + Cloud Function Push)

## Objectives
- Write a pull subscriber (ack/nack).
- Deploy a **push** subscriber as a Cloud Function (this is the correct push pattern).

## 1. Pull subscriber (`code/subscriber.py`)
```python
from google.cloud import pubsub_v1
import json

project_id = "gcp-data-engineering-course"
subscription_id = "cymbal-orders-sub"
subscriber = pubsub_v1.SubscriberClient()
sub_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    try:
        data = json.loads(message.data.decode("utf-8"))
        print(f"Order {data['order_id']} from {data['customer_id']} -> ${data['total_amount']}")
        message.ack()
    except Exception:
        message.nack()   # will be redelivered

future = subscriber.subscribe(sub_path, callback=callback)
print(f"Listening on {sub_path}")
try:
    future.result()
except KeyboardInterrupt:
    future.cancel()
```

## 2. Push subscription → Cloud Function (correct pattern)

Create a Cloud Function, then point a push subscription at its URL:
```powershell
gcloud functions deploy process-order `
  --runtime=python311 --trigger-topic=cymbal-orders `
  --entry-point=process_order `
  --source=code\push_subscriber_function

gcloud pubsub subscriptions create cymbal-orders-push `
  --topic=cymbal-orders `
  --push-endpoint=https://<REGION>-<PROJECT_ID>.cloudfunctions.net/process-order `
  --ack-deadline=60
```

Cloud Function code in `code/push_subscriber_function/main.py`:
```python
import base64, json, logging

def process_order(event, context):
    data = json.loads(base64.b64decode(event["data"]).decode("utf-8"))
    logging.info("Received order %s", data["order_id"])
    return "OK"
```

## Exam notes
- **Pull**: subscriber polls — best for Dataflow/workers (flow control).
- **Push**: Pub/Sub calls an HTTP endpoint — best for Cloud Functions/Run.
- Never point a push subscription at a Dataflow job URL; Dataflow **pulls**.
- Nack (or ack timeout) causes redelivery → design for at-least-once.
