output "buckets" {
  value = {
    raw       = google_storage_bucket.raw.name
    processed = google_storage_bucket.processed.name
  }
}

output "bigquery_dataset" {
  value = google_bigquery_dataset.warehouse.dataset_id
}

output "pubsub_topic" {
  value = google_pubsub_topic.clickstream.name
}
