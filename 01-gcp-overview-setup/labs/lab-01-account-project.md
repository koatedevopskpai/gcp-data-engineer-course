# Lab 01.1 — Create GCP Account and Project

## Objectives
- Create a Google Cloud account (or confirm access).
- Create a project for the course.
- Confirm billing is linked (required even with free credits).

## Steps

### 1. Sign up
1. Go to https://cloud.google.com
2. Click **Get started for free**.
3. Sign in with a Google account.
4. Complete the form and enter a payment method (used for verification only).
5. You receive **$300 credits valid for 90 days**.

### 2. Create a project
1. Open the console: https://console.cloud.google.com
2. Click the project picker (top-left) → **New Project**.
3. Name: `gcp-data-engineering-course`
4. Note the auto-generated **Project ID** (globally unique, used in CLI commands).
5. Click **Create**.

### 3. Link billing
```powershell
gcloud billing accounts list
gcloud billing projects link gcp-data-engineering-course --billing-account=BILLING_ACCOUNT_ID
```

## Validation
```powershell
gcloud projects describe gcp-data-engineering-course
```

## Notes for the exam
- A **project ID** is globally unique and immutable; a **project name** is
  display-only and can change.
- Resources are organized: **Organization → Folders → Projects → Resources**.
