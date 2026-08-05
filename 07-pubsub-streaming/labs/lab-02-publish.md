# Lab 07.2 — Publish Messages (Python)

## Objectives
- Publish JSON messages to a topic with ordering keys.
- Batch and flow-control settings.

## Script (`code/publisher.py`)
```python
from google.cloud import pubsub_v1
import json, random, time

project_id = "gcp-data-engineering-course"
topic_id = "cymbal-orders"

publisher = pubsub_v1.PublisherClient(
    batch_settings=pubsub_v1.types.BatchSettings(max_messages=100, max_bytes=1024 * 1024),
    publisher_options=pubsub_v1.types.PublisherOptions(enable_message_ordering=True),
)
topic_path = publisher.topic_path(project_id, topic_id)

def make_order():
    return {
        "order_id": f"ORD-{random.randint(10000, 99999)}",
        "customer_id": f"CUST-{random.randint(1, 999)}",
        "vendor_id": random.choice(["VTS", "VCM"]),
        "product": random.choice(["Laptop", "Phone", "Tablet", "Headphones"]),
        "quantity": random.randint(1, 5),
        "total_amount": round(random.uniform(10, 1000), 2),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

for i in range(100):
    order = make_order()
    data = json.dumps(order).encode("utf-8")
    future = publisher.publish(topic_path, data, ordering_key=order["customer_id"])
    print(f"[{i+1}] published {order['order_id']}")
    time.sleep(0.2)

publisher.stop()
print("done")
```

## Run
```powershell
python code\publisher.py
```

## Exam notes
- **Ordering keys** require the subscription to have
  `--enable-message-ordering` **and** the publisher client to be created with
  `PublisherOptions(enable_message_ordering=True)` (the client raises
  `ValueError` otherwise).
- Publish **batching** improves throughput; control with `batch_settings`.
- Use **RetrySettings** / flow control to avoid overwhelm.
