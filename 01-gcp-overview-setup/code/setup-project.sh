#!/usr/bin/env bash
# setup-project.sh — create the SA, custom role, budget, and enable APIs.
# Usage: ./setup-project.sh YOUR_PROJECT_ID
set -euo pipefail
PROJECT_ID="${1:?Usage: $0 YOUR_PROJECT_ID}"

echo "==> Configuring project"
gcloud config set project "$PROJECT_ID"

echo "==> Creating service account"
gcloud iam service-accounts create data-engineer-sa --display-name="Data Engineer SA" || true
SA="data-engineer-sa@${PROJECT_ID}.iam.gserviceaccount.com"

echo "==> Granting least-privilege roles"
gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:${SA}" --role="roles/bigquery.jobUser"
gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:${SA}" --role="roles/bigquery.dataEditor"
gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:${SA}" --role="roles/storage.objectAdmin"
gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:${SA}" --role="roles/pubsub.publisher"
gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:${SA}" --role="roles/pubsub.subscriber"
gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:${SA}" --role="roles/dataflow.admin"

echo "==> Creating custom role (optional)"
gcloud iam roles create data_engineer_course --project="$PROJECT_ID" \
  --file=custom-iam-role.json || true

echo "==> Enabling APIs"
gcloud services enable \
  bigquery.googleapis.com storage.googleapis.com dataflow.googleapis.com \
  dataproc.googleapis.com pubsub.googleapis.com composer.googleapis.com \
  cloudfunctions.googleapis.com run.googleapis.com cloudscheduler.googleapis.com \
  workflows.googleapis.com dlp.googleapis.com datacatalog.googleapis.com \
  dataplex.googleapis.com aiplatform.googleapis.com cloudkms.googleapis.com \
  compute.googleapis.com iamcredentials.googleapis.com cloudresourcemanager.googleapis.com

echo "==> Done. Set GOOGLE_APPLICATION_CREDENTIALS=\$PWD/sa-key.json"
