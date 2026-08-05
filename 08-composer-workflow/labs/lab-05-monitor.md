# Lab 08.5 — Monitoring DAGs and Alerting (CORRECTED)

> **Erratum:** the original draft used `gcloud alpha monitoring policies create`
> with an inline condition — that syntax is outdated/broken. Use the console or a
> JSON alerting policy with `gcloud monitoring` (or `gcloud beta`), as below.

## 1. Monitor in Airflow UI
1. Open the Airflow UI (Module 08 Lab 1 URL).
2. DAGs → your DAG → **Grid/Graph** views; open task logs for errors.
3. Check **DAG runs / task instances** states (success/failed/up_for_retry).

## 2. Cloud Logging for Composer
```powershell
# Search Composer logs
gcloud logging read "resource.type=cloud_composer_environment" --limit=50
```

## 3. Create an alerting policy (JSON, correct approach)

Create `code/alerting-policy.json` (valid `gcloud monitoring policies create` format):
```json
{
  "displayName": "Airflow DAG Failure Alert",
  "combiner": "OR",
  "conditions": [
    {
      "displayName": "Composer workflow run failed",
      "conditionThreshold": {
        "filter": "metric.type=\"composer.googleapis.com/workflow/run_count\" AND metric.labels.status=\"failed\"",
        "comparison": "COMPARISON_GT",
        "thresholdValue": 0,
        "duration": "60s",
        "trigger": {
          "count": 1
        }
      }
    }
  ],
  "notificationChannels": []
}
```
> Why this metric: `composer.googleapis.com/workflow/run_count` with
> `status=failed` is a real Composer metric, so the policy actually fires.
> There is no `logging.googleapis.com/user/airflow.dag.failed` metric unless you
> build a log-based metric from Composer logs first.

Upload and enable:
```powershell
gcloud beta monitoring policies create --policy-from-file=code\alerting-policy.json
```

Clean up after the lab:
```powershell
gcloud beta monitoring policies delete <POLICY_ID>
```

## Alternative (console — most reliable for students)
1. Monitoring → **Alerting → Create policy**.
2. Select metric `Composer > Workflow > run_count` filtered on status=failed.
3. Threshold: value ≥ 1 for 0s. Add notification channel (email).

## Exam notes
- Composer surfaces DAG status via the `composer.googleapis.com` metrics.
- Alert on **task state** (failed) rather than DAG state for finer signals.
