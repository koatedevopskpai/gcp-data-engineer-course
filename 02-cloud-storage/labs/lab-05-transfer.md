# Lab 02.5 — Transferring Data: Storage Transfer Service & Transfer Appliance

## Objectives
- Move data into GCS from HTTP(S) and from another bucket / S3.
- Understand when to use Transfer Appliance (offline).

## 1. Storage Transfer Service — HTTP/HTTPS source

```powershell
$PROJECT_ID = "gcp-data-engineering-course"

gcloud transfer jobs create gs://cymbal-raw-$PROJECT_ID/sample-transactions/ `
  --source-uri="https://storage.googleapis.com/cloud-samples-data/bigquery/sample-transactions/" `
  --schedule-repeats=daily

# run once immediately
gcloud transfer jobs run <JOB_NAME>
```

## 2. Storage Transfer Service — S3 or another bucket

```powershell
# S3 requires HMAC credentials configured in the console or via the API.
gcloud transfer jobs create gs://cymbal-raw-$PROJECT_ID/s3/ `
  --source-uri="s3://my-source-bucket/data/" `
  --source-agent-pool-name=default `
  --schedule-repeats=every-24-hours
```

## 3. Transfer Appliance (offline migration)

- Use when: >20 TB and slow network, or data is hard to upload online.
- Google ships a physical appliance; you load data, ship it back; data is
  copied into GCS and the appliance is wiped.

## Decision table (exam-favorite)

| Scenario | Best tool |
|---|---|
| 100 TB over a limited WAN | **Transfer Appliance** (offline) |
| Continuous sync from on-prem/S3 to GCS | **Storage Transfer Service** |
| One-off copy of a few files | `gsutil cp` / `rsync` |
| Data in another GCS bucket | Storage Transfer Service or `gsutil` |
| <5 TB, quick, single site | `gsutil rsync` |

## Exam notes
- **Transfer Appliance** and **Storage Transfer Service** are the two official
  migration answers. If the question says "network bandwidth is limited", pick
  Transfer Appliance. If it says "ongoing/periodic", pick Transfer Service.
