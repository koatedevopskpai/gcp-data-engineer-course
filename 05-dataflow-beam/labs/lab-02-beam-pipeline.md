# Lab 05.2 — Write a Custom Python Beam Pipeline (Batch ETL)

## Objectives
- Write a batch Beam pipeline: read CSV from GCS → clean → write to BigQuery.
- Run locally (DirectRunner) and on Dataflow (DataflowRunner).

## Files
- `code/taxi_etl_pipeline.py` — the pipeline
- `code/requirements.txt` — worker dependencies (needed for Dataflow)

## Run locally first
```powershell
$env:PROJECT_ID = "gcp-data-engineering-course"
python code\taxi_etl_pipeline.py --runner=DirectRunner
```

## Run on Dataflow
```powershell
python code\taxi_etl_pipeline.py `
  --runner=DataflowRunner `
  --project=gcp-data-engineering-course `
  --region=us-central1 `
  --temp_location=gs://cymbal-processed-gcp-data-engineering-course/dataflow/temp `
  --staging_location=gs://cymbal-processed-gcp-data-engineering-course/dataflow/staging `
  --max_num_workers=2 `
  --autoscaling_algorithm=THROUGHPUT_BASED
```

## Pipeline highlights
```python
lines  = p | "ReadCSV" >> beam.io.ReadFromText(INPUT, skip_header_lines=1)
parsed = lines | "ParseCSV" >> beam.ParDo(ParseCSV())
clean  = parsed | "CleanData" >> beam.ParDo(CleanData())
clean  | "WriteToBigQuery" >> WriteToBigQuery(...)
```

## Exam notes
- `ParDo` = element-wise transform (a `DoFn`); `Map`/`FlatMap` are sugar.
- `CombinePerKey`, `GroupByKey` and **side inputs** are the core PTransform toolkit.
- Dataflow service account needs `roles/dataflow.worker` + the data permissions.
