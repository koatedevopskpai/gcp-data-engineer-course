#!/usr/bin/env python
"""Pull subscriber with ack/nack."""
import json
import os

from google.cloud import pubsub_v1

PROJECT_ID = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")
SUBSCRIPTION_ID = "cymbal-orders-sub"

subscriber = pubsub_v1.SubscriberClient()
sub_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)


def callback(message):
    try:
        data = json.loads(message.data.decode("utf-8"))
        print(f"Order {data['order_id']} from {data['customer_id']} -> ${data['total_amount']}")
        message.ack()
    except Exception:
        message.nack()


def main() -> None:
    future = subscriber.subscribe(sub_path, callback=callback)
    print(f"Listening on {sub_path}")
    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()


if __name__ == "__main__":
    main()
