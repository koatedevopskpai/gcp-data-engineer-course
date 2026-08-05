# Module 05 — Dataflow & Apache Beam

Unified batch + streaming processing. Write a Beam pipeline once, run it on the
local runner or on Dataflow.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-wordcount-template.md` | First Dataflow job (WordCount template) |
| `labs/lab-02-beam-pipeline.md` | Custom batch ETL: GCS CSV → BigQuery |
| `labs/lab-03-streaming.md` | Streaming: Pub/Sub → windows/triggers → BigQuery |
| `labs/lab-04-side-inputs.md` | Side inputs / `CombinePerKey` / `GroupByKey` |
| `labs/lab-05-flex-template.md` | Dataflow Flex Templates |
| `code/taxi_etl_pipeline.py` | Batch ETL pipeline (verified on GCP) |
| `code/streaming_taxi_pipeline.py` | Streaming pipeline (subscription-pull based) |
| `code/side_input_pipeline.py` | Side-input enrichment example |
| `code/wordcount.py` | Minimal `wordcount` reference |
| `code/flex_template_pipeline.py` | Flex template entrypoint |
| `code/requirements.txt` | Worker dependencies for Dataflow |
| `exercises/exercises.md` | Self-check questions |

## Run on Dataflow

```powershell
python code\taxi_etl_pipeline.py `
  --runner=DataflowRunner `
  --project=gcp-data-engineering-course `
  --region=us-central1 `
  --service_account_email=data-engineer-sa@gcp-data-engineering-course.iam.gserviceaccount.com `
  --temp_location=gs://cymbal-processed-gcp-data-engineering-course/dataflow/temp `
  --staging_location=gs://cymbal-processed-gcp-data-engineering-course/dataflow/staging `
  --max_num_workers=2
```

Run the job as `data-engineer-sa` (Terraform grants it
`roles/dataflow.worker`, `storage.objectAdmin`, `bigquery.dataEditor`,
`bigquery.jobUser`).

## Known gotchas (verified on Beam 2.75)

- **`beam.Pipeline()` ignores command-line flags.** Build
  `PipelineOptions()` explicitly and pass `options=` — otherwise `--runner`
  is dropped and the job silently runs on the local (Prism) runner.
- Batch `WriteToBigQuery` uses FILE_LOADS and needs a GCS temp location
  (`custom_gcs_temp_location` or `--temp_location`).
- Dataflow worker capacity: `us-central1` has been seeing
  `ZONE_RESOURCE_POOL_EXHAUSTED`; pin `--zone` and/or a small machine type
  (e.g. `--worker_machine_type=e2-standard-2`).

## Exam notes

- Beam primitives: `PCollection`, `PTransform`, `ParDo` (DoFn), `Map`/`FlatMap`,
  `GroupByKey`, `CombinePerKey`, side inputs/outputs.
- **Windows** (fixed/sliding/session) + **triggers** (default, allowed
  lateness, accumulating/discarding) govern streaming output.
- Streaming pipelines are always-on — cancel Dataflow jobs after labs.
