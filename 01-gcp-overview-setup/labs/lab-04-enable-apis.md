# Lab 01.4 — Enable Required APIs

## Objectives
- Enable every API used by the course.
- Verify the enabled list.

## Steps
```powershell
$PROJECT_ID = "gcp-data-engineering-course"
gcloud config set project $PROJECT_ID

gcloud services enable --project=$PROJECT_ID `
  bigquery.googleapis.com `
  bigqueryconnection.googleapis.com `
  storage.googleapis.com `
  dataflow.googleapis.com `
  dataproc.googleapis.com `
  pubsub.googleapis.com `
  composer.googleapis.com `
  cloudfunctions.googleapis.com `
  run.googleapis.com `
  cloudscheduler.googleapis.com `
  workflows.googleapis.com `
  dlp.googleapis.com `
  datacatalog.googleapis.com `
  dataplex.googleapis.com `
  aiplatform.googleapis.com `
  cloudkms.googleapis.com `
  compute.googleapis.com `
  iamcredentials.googleapis.com `
  cloudresourcemanager.googleapis.com
```

## Verify
```powershell
gcloud services list --enabled
```

## Exam notes
- Enabling APIs is free; you pay per use.
- Each service generally needs its own API enabled before first use
  (e.g., `dataproc.googleapis.com` before creating a cluster).
