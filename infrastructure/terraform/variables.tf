variable "project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "GCP Region"
  type        = string
  default     = "us-central1"
}

variable "bucket_prefix" {
  description = "Bucket name prefix (keep global-uniqueness in mind)"
  type        = string
  default     = "cymbal"
}
