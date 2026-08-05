#!/usr/bin/env python
"""Publish simulated orders with ordering keys."""
import json
import random
import time

from google.cloud import pubsub_v1

PROJECT_ID = "gcp-data-engineering-course"
TOPIC_ID = "cymbal-orders"

publisher = pubsub_v1.PublisherClient(
    batch_settings=pubsub_v1.types.BatchSettings(max_messages=100, max_bytes=1024 * 1024)
)
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)


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


def main() -> None:
    for i in range(100):
        order = make_order()
        data = json.dumps(order).encode("utf-8")
        future = publisher.publish(topic_path, data, ordering_key=order["customer_id"])
        print(f"[{i+1}] published {order['order_id']}")
        time.sleep(0.2)
    publisher.close()
    print("done")


if __name__ == "__main__":
    main()
