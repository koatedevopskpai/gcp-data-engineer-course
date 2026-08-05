#!/usr/bin/env python
"""Simulates Cymbal Retail website clickstream -> Pub/Sub."""
import json
import os
import random
import time
from datetime import datetime, timezone

from google.cloud import pubsub_v1

PROJECT_ID = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")
TOPIC_ID = "cymbal-clickstream"

PRODUCTS = ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch", "Camera"]
PAGES = ["/home", "/products", "/cart", "/checkout", "/account"]
ACTIONS = ["view", "click", "add_to_cart", "purchase"]


def generate_event() -> dict:
    return {
        "event_id": f"EVT-{random.randint(100000, 999999)}",
        "user_id": f"USER-{random.randint(1000, 9999)}",
        "session_id": f"SESS-{random.randint(1000, 9999)}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "page": random.choice(PAGES),
        "product": random.choice(PRODUCTS),
        "action": random.choice(ACTIONS),
        "value": round(random.uniform(0, 500), 2),
    }


def main() -> None:
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)
    print(f"Publishing to {topic_path}")
    try:
        while True:
            event = generate_event()
            data = json.dumps(event).encode("utf-8")
            publisher.publish(topic_path, data)
            print(f"Published {event['event_id']} - {event['action']}")
            time.sleep(random.uniform(0.1, 1.0))
    except KeyboardInterrupt:
        publisher.close()
        print("Stopped.")


if __name__ == "__main__":
    main()
