#!/usr/bin/env bash
# gsutil-commands.sh — reference for Module 02 commands.
set -e
PROJECT_ID="${1:?Usage: $0 YOUR_PROJECT_ID}"
BUCKET="gs://cymbal-raw-${PROJECT_ID}"

echo "==> Create + configure raw bucket"
gsutil mb -l us-central1 "${BUCKET}"
gsutil versioning set on "${BUCKET}"
gsutil lifecycle set lifecycle-policy.json "${BUCKET}"

echo "==> Uploads"
echo "a,b,c" | gsutil cp - gs://cymbal-raw-${PROJECT_ID}/sample.csv
gsutil cp gs://cloud-samples-data/bigquery/sample-transactions/* "${BUCKET}/"

echo "==> Permissions"
gsutil uniformbucketlevelaccess set on "${BUCKET}"
gsutil iam ch "serviceAccount:data-engineer-sa@${PROJECT_ID}.iam.gserviceaccount.com:objectViewer" "${BUCKET}"
