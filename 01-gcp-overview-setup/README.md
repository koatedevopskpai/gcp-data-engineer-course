# Module 01 — GCP Overview & Project Setup

Set up the Google Cloud foundation used by every later module: account, project,
IAM, enabled APIs, and cost controls.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-account-project.md` | Create GCP account + billing project |
| `labs/lab-02-gcloud-install.md` | Install / initialize the `gcloud` CLI |
| `labs/lab-03-service-account.md` | Create a service account + key for scripts |
| `labs/lab-04-enable-apis.md` | Enable the APIs the course needs |
| `labs/lab-05-budget-cost-control.md` | Budget, alerts, and cost controls |
| `code/setup-project.sh` | One-shot project bootstrap (APIs + config) |
| `code/custom-iam-role.json` | Reusable custom IAM role definition |
| `exercises/exercises.md` | Self-check questions |

## TL;DR

```bash
gcloud config set project YOUR_PROJECT_ID
gcloud services enable storage.googleapis.com bigquery.googleapis.com \
  pubsub.googleapis.com dataflow.googleapis.com \
  dataproc.googleapis.com composer.googleapis.com \
  dlp.googleapis.com datacatalog.googleapis.com \
  aiplatform.googleapis.com
```

Create a **budget + alert** before any paid lab (Lab 05). Enable the same APIs
on a fresh project before running Module 04+ labs.

## Exam notes

- IAM = who (member) can do what (role) on which resource; roles can be
  primitive, predefined, or **custom** (curated permissions only).
- Service accounts are the identity for code, not humans; keys are long-lived
  secrets — prefer Workload Identity / ADC where possible.
- Billing budgets are for **alerts**, not hard limits.
