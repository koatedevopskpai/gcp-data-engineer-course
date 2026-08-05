# Prerequisites

## Google Cloud account

- A Google (Gmail/Workspace) account.
- A **new** cloud account qualifies for **$300 credits / 90 days**:
  https://cloud.google.com/free
- A credit card is required at signup for verification, but you will stay
  under the free-credit amount if you follow the cost policy.

## Hardware / OS

- 8 GB RAM (16 GB recommended).
- 20 GB free disk.
- Any OS: **Windows (10/11), macOS, or Linux**.
- For Windows, PowerShell is used throughout. WSL2 also works for the bash scripts.

## Software

| Tool | Version | Install |
|---|---|---|
| Google Cloud SDK (`gcloud`, `gsutil`, `bq`) | latest | https://cloud.google.com/sdk/docs/install (Windows: installer or `choco install googlecloudsdk`) |
| Python | 3.10 – 3.12 | https://www.python.org/downloads/ |
| pip | latest | bundled with Python |
| Git | latest | https://git-scm.com/ |
| (Optional) Terraform | 1.5+ | https://developer.hashicorp.com/terraform/downloads |
| (Optional) Docker | latest | for local Airflow/Dataproc testing |

## Recommended Python packages (installed via requirements.txt)

- `google-cloud-bigquery`, `google-cloud-storage`, `google-cloud-pubsub`,
  `google-cloud-dlp`, `google-cloud-aiplatform`
- `apache-beam[gcp]`
- `pyspark` (only needed if running Spark locally)
- `dbt-bigquery`
- `google-api-python-client`, `google-auth`, `pandas`, `numpy`

## BigQuery quota notes

- The always-free tier includes **1 TB of BigQuery query processing per month**.
- Keep `--dry_run` in mind for cost checks during the course.
