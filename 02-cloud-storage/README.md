# Module 02 — Cloud Storage

Object storage foundation: buckets, lifecycle policies, permissions, CMEK
encryption, and transfers. Hosts the course's canonical `taxi_trips.csv`.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-create-bucket-lifecycle.md` | Buckets + lifecycle rules (NEARLINE, delete) |
| `labs/lab-02-upload-objects.md` | `gsutil` upload/download/versioning |
| `labs/lab-03-permissions.md` | Uniform bucket-level access + IAM |
| `labs/lab-04-cmek.md` | Customer-managed encryption keys (KMS) |
| `labs/lab-05-transfer.md` | Storage Transfer Service / `gsutil rsync` |
| `code/gsutil-commands.sh` | Cheat-sheet of every `gsutil` command used |
| `code/lifecycle-policy.json` | JSON lifecycle policy example |
| `datasets/taxi_trips.csv` | Canonical 40-row taxi dataset (see `datasets/README.md`) |
| `exercises/exercises.md` | Self-check questions |

## Data contract

`datasets/README.md` documents the canonical source:
- **Canonical**: the bundled `datasets/taxi_trips.csv` (40 rows) — header matches
  `03-bigquery-fundamentals/code/schema.json` and the module 5/6 pipelines.
- **Optional big dataset**: NYC TLC CDN parquet (`yellow_tripdata_2024-01.parquet`).
- The legacy `gs://nyc-tlc/...` URLs in the original draft are **dead** and removed.

## TL;DR

```bash
gsutil mb -p YOUR_PROJECT_ID -l us-central1 gs://cymbal-raw-YOUR_PROJECT_ID
gsutil cp 02-cloud-storage/datasets/taxi_trips.csv gs://cymbal-raw-YOUR_PROJECT_ID/taxi/
```

## Exam notes

- Buckets are global names, regional/dual-region/multi-region location types.
- **Storage classes**: Standard, Nearline (30d), Coldline (90d), Archive (365d)
  — lifecycle rules move objects between them; minimum-duration charges apply.
- **Versioning + lifecycle** protect against deletion; `lifecycle_rule` in
  Terraform uses nested `action { type }` blocks (a semicolon form is invalid).
