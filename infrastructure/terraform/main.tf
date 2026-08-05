# Shared course infrastructure (buckets, BQ, Pub/Sub, SA + IAM).

data "google_project" "project" {
  project_id = var.project_id
}

resource "google_storage_bucket" "raw" {
  name                        = "${var.bucket_prefix}-raw-${var.project_id}"
  location                    = var.region
  force_destroy               = true
  uniform_bucket_level_access = true
  versioning {
    enabled = true
  }
  lifecycle_rule {
    action {
      type          = "SetStorageClass"
      storage_class = "NEARLINE"
    }
    condition {
      age = 30
    }
  }
  lifecycle_rule {
    action { type = "Delete" }
    condition { age = 365 }
  }
}

resource "google_storage_bucket" "processed" {
  name                        = "${var.bucket_prefix}-processed-${var.project_id}"
  location                    = var.region
  force_destroy               = true
  uniform_bucket_level_access = true
}

resource "google_bigquery_dataset" "warehouse" {
  dataset_id                  = "cymbal_warehouse"
  location                    = var.region
  default_table_expiration_ms = 1000 * 60 * 60 * 24 * 365
  delete_contents_on_destroy  = true
}

resource "google_pubsub_topic" "clickstream" {
  name = "cymbal-clickstream"
}

resource "google_pubsub_subscription" "clickstream_sub" {
  name                         = "clickstream-sub"
  topic                        = google_pubsub_topic.clickstream.name
  ack_deadline_seconds         = 60
  enable_exactly_once_delivery = true
  enable_message_ordering      = true
}

resource "google_service_account" "data_engineer" {
  account_id   = "data-engineer-sa"
  display_name = "Data Engineer Course SA"
}

resource "google_project_iam_member" "bq_job_user" {
  project = var.project_id
  role    = "roles/bigquery.jobUser"
  member  = "serviceAccount:${google_service_account.data_engineer.email}"
}

resource "google_project_iam_member" "bq_data_editor" {
  project = var.project_id
  role    = "roles/bigquery.dataEditor"
  member  = "serviceAccount:${google_service_account.data_engineer.email}"
}

resource "google_project_iam_member" "storage_object_admin" {
  project = var.project_id
  role    = "roles/storage.objectAdmin"
  member  = "serviceAccount:${google_service_account.data_engineer.email}"
}

resource "google_project_iam_member" "pubsub_editor" {
  project = var.project_id
  role    = "roles/pubsub.editor"
  member  = "serviceAccount:${google_service_account.data_engineer.email}"
}

resource "google_project_iam_member" "dataflow_worker" {
  project = var.project_id
  role    = "roles/dataflow.worker"
  member  = "serviceAccount:${google_service_account.data_engineer.email}"
}

resource "google_service_account_iam_member" "data_engineer_impersonator" {
  service_account_id = google_service_account.data_engineer.name
  role               = "roles/iam.serviceAccountUser"
  member             = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com"
}
