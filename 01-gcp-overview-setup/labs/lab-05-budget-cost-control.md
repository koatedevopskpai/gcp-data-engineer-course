# Lab 01.5 — Budgets, Alerts and Cost Control (required before every lab)

> This is the most important lab in the course. It keeps you inside the
> $300 free credits. Run it once, at the start.

## Objectives
- Create a project-level budget with email alerts.
- Understand the expensive services and their shutdown procedures.

## 1. Create a budget

Console: **Billing → Budgets & alerts → Create budget**

- Scope: the project `gcp-data-engineering-course`
- Amount: **$60** (safely under the $300 free credits)
- Alerts: 50%, 75%, 90%, 100% → notify your email

CLI (current):
```bash
gcloud billing budgets create --billing-account=BILLING_ACCOUNT_ID \
  --display-name="Course Budget" --budget-amount=60 \
  --threshold-rule=percent=0.5 --threshold-rule=percent=0.75 \
  --threshold-rule=percent=0.9 --threshold-rule=percent=1.0 \
  --filter-projects=projects/gcp-data-engineering-course
```

## 2. Expensive resources — always delete after the lab

| Resource | Command to clean up |
|---|---|
| Dataproc cluster | `gcloud dataproc clusters delete taxi-cluster --region=us-central1` |
| Composer environment | `gcloud composer environments delete data-pipeline-env --location=us-central1` |
| Dataflow streaming job | `gcloud dataflow jobs cancel JOB_ID --region=us-central1` |
| Vertex AI endpoint | `gcloud ai endpoints delete ENDPOINT_ID --region=us-central1` |
| BigQuery reservation | `bq mk --reservation ... ` then delete / cancel commitment |
| Cloud Run/CF instances | stop/delete the service |

## 3. Guardrails you can enable

- `gcloud dataproc clusters create ... --max-idle=20m --max-idle` auto-deletes an idle cluster.
- Set **BigQuery default table expiration** on datasets:
  ```sql
  ALTER SCHEMA cymbal_warehouse SET OPTIONS(default_table_expiration_days=180);
  ```
- Use preemptible Dataproc workers (`--num-preemptible-workers=2`).

## Validation
- Verify you receive a test email from Billing.
- Confirm the budget appears in Billing → Budgets & alerts.
