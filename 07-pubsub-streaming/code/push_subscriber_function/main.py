#!/usr/bin/env python
"""Cloud Function push subscriber. This is the CORRECT push pattern
(Pub/Sub -> HTTP endpoint). Dataflow pipelines pull instead."""
import base64
import json
import logging


def process_order(event, context):
    try:
        data = json.loads(base64.b64decode(event["data"]).decode("utf-8"))
        logging.info("Received order %s from %s", data["order_id"], data["customer_id"])
    except Exception as exc:  # noqa: BLE001
        logging.error("Failed to decode message: %s", exc)
        raise
    return "OK"
