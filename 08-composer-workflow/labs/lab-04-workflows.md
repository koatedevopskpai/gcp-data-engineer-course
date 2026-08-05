# Lab 08.4 — Google Cloud Workflows (serverless orchestration)

## Objectives
- Write a YAML workflow: HTTP fetch → BigQuery transform → notification.
- Deploy and execute with `gcloud`.

## 1. Workflow definition (`code/workflows/etl_workflow.yaml`)
```yaml
main:
  params: [input]
  steps:
    - fetch:
        call: http.get
        args:
          url: https://api.example.com/data
        result: raw_data

    - transform:
        call: googleapis.bigquery.v2.jobs.query
        args:
          projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT")}
          body:
            query: |
              CREATE OR REPLACE TABLE `cymbal_warehouse.staging` AS
              SELECT * FROM UNNEST(@rows)
            parameterMode: NAMED
            queryParameters:
              - name: rows
                parameterType: { type: ARRAY }
                parameterValue: { arrayValue: { values: ${raw_data.body.items} } }

    - notify:
        call: googleapis.logging.v2.entries.write
        args:
          entries:
            - logName: "projects/${sys.get_env('GOOGLE_CLOUD_PROJECT')}/logs/workflow"
              textPayload: "Workflow finished"
```

## 2. Deploy + run
```powershell
gcloud workflows deploy etl-workflow `
  --source=code\workflows\etl_workflow.yaml `
  --location=us-central1

gcloud workflows run etl-workflow --location=us-central1 `
  --data='{"input": {"hello": "world"}}'
```

## 3. Schedule with Cloud Scheduler
```powershell
gcloud scheduler jobs create http daily-etl `
  --schedule="0 6 * * *" `
  --uri="https://workflowexecutions.googleapis.com/v1/projects/gcp-data-engineering-course/locations/us-central1/workflows/etl-workflow/executions" `
  --http-method=POST `
  --oauth-service-account-email=data-engineer-sa@gcp-data-engineering-course.iam.gserviceaccount.com
```

## Decision: orchestration tools (exam-favorite)

| Need | Tool |
|---|---|
| Complex dependencies, retries, backfills, many operators | **Cloud Composer (Airflow)** |
| Simple linear serverless automation, low cost, no VMs | **Cloud Workflows** |
| Run one job on a schedule | **Cloud Scheduler** |
| React to events (GCS/Pub/Sub) | **Eventarc** |
