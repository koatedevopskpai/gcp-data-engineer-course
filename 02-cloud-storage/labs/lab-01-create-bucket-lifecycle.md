# Lab 02.1 — Create Buckets with Lifecycle Policy + Versioning

## Objectives
- Create raw and processed buckets.
- Enable versioning.
- Apply a lifecycle policy (Nearline after 30 days, delete after 365 days).

## Steps (Windows PowerShell)

```powershell
$PROJECT_ID = "gcp-data-engineering-course"

# 1. Create buckets (names must be globally unique)
gsutil mb -l us-central1 gs://cymbal-raw-$PROJECT_ID
gsutil mb -l us-central1 gs://cymbal-processed-$PROJECT_ID

# 2. Enable versioning on raw bucket
gsutil versioning set on gs://cymbal-raw-$PROJECT_ID

# 3. Apply lifecycle policy
gsutil lifecycle set code/lifecycle-policy.json gs://cymbal-raw-$PROJECT_ID

# 4. Verify
gsutil lifecycle get gs://cymbal-raw-$PROJECT_ID
gsutil versioning get gs://cymbal-raw-$PROJECT_ID
```

## Lifecycle policy (`code/lifecycle-policy.json`)
Moves live objects older than 30 days to Nearline and deletes them at 365 days.

## Exam notes
- **Storage classes:** Standard (hot), Nearline (30-day min), Coldline (90-day
  min), Archive (365-day min). Min periods = minimum billing duration.
- Lifecycle rules can change class or delete; conditions include age, createdBefore,
  numNewerVersions, matchesStorageClass, isLive, and custom time.
- **Versioning** + lifecycle `numNewerVersions` is a common backup pattern.
