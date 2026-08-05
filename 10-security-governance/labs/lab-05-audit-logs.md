# Lab 10.5 — Cloud Audit Logs & Export

## Objectives
- Create a log sink that exports BigQuery audit logs to a dataset.
- Query access logs.

## 1. Create dataset + sink
```powershell
bq mk --dataset audit_logs

gcloud logging sinks create bigquery-audit-sink `
  bigquery.googleapis.com/projects/gcp-data-engineering-course/datasets/audit_logs `
  --log-filter='protoPayload.serviceName="bigquery.googleapis.com"'

# Grant the sink writer permission (prints a service account to authorize)
gcloud logging sinks describe bigquery-audit-sink
bq show --format=prettyjson audit_logs   # add the sink SA as WRITER on the dataset if prompted
```

## 2. Query the exported logs
```sql
SELECT
  protopayload_auditlog.authenticationInfo.principalEmail AS user,
  protopayload_auditlog.methodName                         AS method,
  protopayload_auditlog.resourceName                       AS resource,
  timestamp
FROM `gcp-data-engineering-course.audit_logs.cloudaudit_googleapis_com_data_access_*`
WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
ORDER BY timestamp DESC
LIMIT 100;
```

## 3. Audit log types (exam)
| Type | Content |
|---|---|
| **Admin activity** | resource configuration changes (always on, 400-day retention) |
| **Data access** | reads/writes of data (off by default, 400-day retention) |
| **System event** | Google system actions on resources |
| **Policy denied** | explicit/denied IAM decisions |

## Exam notes
- Use a **sink** (filtered) → BigQuery / Storage / Pub/Sub for long-term export
  or real-time alerts.
- Enable **data access logs** for tracking who read data (cost consideration).
