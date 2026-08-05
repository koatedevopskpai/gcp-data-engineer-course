# Lab 10.3 — VPC Service Controls Perimeter

## Objectives
- Create a service perimeter around BigQuery/Storage.
- Start in **dry-run** mode, then enforce.

> Requires an Organization. If you only have free credits (no org), complete this
> lab in dry-run mode conceptually, or skip the enforced step.

## Steps
```powershell
# 1. Ensure the Access Context Manager API is on
gcloud services enable accesscontextmanager.googleapis.com

# 2. Get or create an access policy
gcloud access-context-manager policies create --organization=ORG_ID --title="Data Policy"
gcloud access-context-manager policies list

# 3. Create the perimeter (dry-run first — set --dry-run via gcloud --beta/perimeter config)
gcloud beta access-context-manager perimeters create data_perimeter `
  --policy=POLICY_ID `
  --title="Data Engineering Perimeter" `
  --resources=projects/123456789012 `
  --restricted-services=bigquery.googleapis.com,storage.googleapis.com `
  --vpc-allowed-services=bigquery.googleapis.com,storage.googleapis.com
```

## Enforce vs dry-run
- **Dry-run mode**: perimeter defined, but violations are only logged.
- **Enforced**: access outside the perimeter is denied.

## Exam notes
- **VPC-SC** prevents **data exfiltration** — a service inside the perimeter
  cannot copy data outside it (even to an attacker's bucket).
- Applies to supported services (BigQuery, GCS, Dataflow, ...) — "restricted services".
- **Cloud NAT/VPC** still work for network egress of APIs; VPC-SC is data-plane control.
