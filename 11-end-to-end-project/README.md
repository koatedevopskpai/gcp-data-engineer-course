# Cymbal Retail — End-to-End Project

Production-style streaming analytics platform.

## Prerequisites
Modules 1–10 completed; buckets + `cymbal_warehouse` dataset exist.

## Setup
```powershell
# 1. Pub/Sub topic + subscription
gcloud pubsub topics create cymbal-clickstream
gcloud pubsub subscriptions create clickstream-sub --topic=cymbal-clickstream --ack-deadline=60

# 2. BigQuery tables are created by the pipeline (CREATE_IF_NEEDED)
```

## Run
```powershell
# Terminal 1 — simulate clickstream
python code\simulator.py

# Terminal 2 — streaming pipeline (Dataflow)
python code\streaming_pipeline.py `
  --runner=DataflowRunner --project=gcp-data-engineering-course --region=us-central1 `
  --streaming `
  --temp_location=gs://cymbal-processed-gcp-data-engineering-course/dataflow/temp `
  --max_num_workers=2
```

## dbt transforms
```bash
cd dbt
dbt deps && dbt run
```
> `stg_events` materializes as a view in `<project>.cymbal_warehouse_staging`,
> `fct_daily_sales` as a table in `<project>.cymbal_warehouse_marts`.

## Deliverables checklist
- [ ] Clickstream simulator publishing to Pub/Sub
- [ ] Dataflow pipeline writing Bronze + Gold tables
- [ ] dbt models (stg_events, fct_daily_sales) with tests
- [ ] Composer hourly DAG (`code/dags/end_to_end_dag.py`)
- [ ] Looker Studio dashboard (3 pages)
- [ ] Architecture diagram (`architecture/architecture.md`)

## Cleanup (always)
```powershell
gcloud dataflow jobs cancel <JOB_ID> --region=us-central1
gcloud composer environments delete data-pipeline-env --location=us-central1
gcloud pubsub subscriptions delete clickstream-sub
```
