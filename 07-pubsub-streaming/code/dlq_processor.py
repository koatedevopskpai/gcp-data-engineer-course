#!/usr/bin/env python
"""Process messages in the dead-letter queue."""
import json

from google.cloud import pubsub_v1

PROJECT_ID = "gcp-data-engineering-course"
SUBSCRIPTION_ID = "cymbal-orders-dlq-sub"

subscriber = pubsub_v1.SubscriberClient()
sub_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)


def process_dlq(message):
    data = json.loads(message.data.decode("utf-8"))
    print(f"DLQ: {data['order_id']} attempt={message.delivery_attempt}")
    message.ack()


def main() -> None:
    future = subscriber.subscribe(sub_path, callback=process_dlq)
    print(f"Watching DLQ on {sub_path}")
    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()


if __name__ == "__main__":
    main()
