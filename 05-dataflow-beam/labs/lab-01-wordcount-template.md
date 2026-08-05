# Lab 05.1 — Run the Built-in WordCount Template

## Objectives
- Run a Google-provided Dataflow template (no code needed).
- Inspect the job in the console and in `gcloud`.

## Steps

```powershell
$PROJECT_ID = "gcp-data-engineering-course"
$BUCKET = "gs://cymbal-processed-$PROJECT_ID"

# Run the classic Word_Count template
gcloud dataflow jobs run wordcount-job `
  --region=us-central1 `
  --gcs-location gs://dataflow-templates/latest/Word_Count `
  --parameters "inputFiles=gs://dataflow-samples/shakespeare/kinglear.txt,output=${BUCKET}/wordcount/output"

# Check status
gcloud dataflow jobs list --region=us-central1
```

## Cleanup
```powershell
gcloud dataflow jobs cancel wordcount-job --region=us-central1
# or let the batch job finish (it terminates itself)
```

## Exam notes
- **Classic templates** vs **Flex templates** — Flex supports any SDK/container
  and custom dependencies; classic is Python/Java prebuilt.
- Dataflow autoscales workers; batch jobs terminate when done, streaming jobs run
  until cancelled.
