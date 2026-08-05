#!/usr/bin/env python
"""Vertex AI batch prediction example."""
import os

from google.cloud import aiplatform

PROJECT = os.environ.get("PROJECT_ID", "gcp-data-engineering-course")
LOCATION = "us-central1"
MODEL_ID = "MODEL_ID"  # from `gcloud ai models list`


def main() -> None:
    aiplatform.init(project=PROJECT, location=LOCATION)
    model = aiplatform.Model(
        f"projects/{PROJECT}/locations/{LOCATION}/models/{MODEL_ID}"
    )
    batch_job = model.batch_predict(
        job_display_name="fare_batch_prediction",
        gcs_source=f"gs://cymbal-raw-{PROJECT}/predictions/input.jsonl",
        gcs_destination_prefix=f"gs://cymbal-processed-{PROJECT}/predictions/",
        machine_type="n1-standard-2",
    )
    batch_job.wait()
    print("Done. Results in gs://cymbal-processed-<PROJECT>/predictions/")


if __name__ == "__main__":
    main()
