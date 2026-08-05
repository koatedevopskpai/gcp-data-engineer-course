# Google Cloud Professional Data Engineer — Complete Course Package (CORRECTED MASTER)

> **Purpose of this document**
> This is the corrected, exam-aligned master for the Udemy course "GCP Data Engineer Professional – Project & Exam Prep".
> It fixes the errors in the original draft, closes the gaps versus the official
> [Professional Data Engineer exam guide](https://cloud.google.com/certification/data-engineer), and
> points to the runnable code/artifacts delivered alongside it.
>
> The original file `gcp-data-professional-exam-prep_Udemy_Course.txt` is preserved for reference; this
> document supersedes it.

---

## 0. Exam facts (keep current at publication)

- **Certification:** Google Cloud Professional Data Engineer
- **Exam:** 2 hours, ~50 multiple-choice questions, may include case studies
- **Cost:** $200 USD per attempt
- **Free credits for labs:** https://cloud.google.com/free ($300 / 90 days)
- **Recommended lab budget strategy:** stay under ~$60 actual spend by using the cost controls in Module 1 Lab 5 and by deleting/stopping resources after every lab.

### Skills measured (official weighting)

| Skill area | Weight |
|---|---|
| Design data processing systems | 20–25% |
| Build and operationalize data processing | 30–35% |
| Operationalize machine learning models | 15–20% |
| Ensure solution quality (data quality & governance, cost, reliability, security) | 15–20% |

### Why this course was restructured

1. **ML was missing** → new **Module 13: BigQuery ML & Vertex AI** (the 15–20% ML domain).
2. **Case studies are on the exam** → Module 12 adds case-study practice + 2 full-length mocks.
3. **High-yield services were missing** → Cloud Bigtable, Dataform, Dataplex, federated/external tables, slots/capacity are now covered (Modules 3, 4, 10).
4. **Cost feasibility** → explicit cost-control labs (budgets, preemptible VMs, auto-delete, stop-after-lab).
5. **Technical errors fixed** → see "Errata (what was wrong and how it is fixed)" below.

---

## Errata — errors in the original draft and their fixes

| # | Original (wrong) | Fix (now in this package) | Where |
|---|---|---|---|
| 1 | "Create push subscription to Dataflow" — you cannot push into a Dataflow job; Dataflow *pulls* from Pub/Sub | Module 7 Lab 4 now: Dataflow pulls from a Pub/Sub subscription; push subscriptions are demonstrated against a Cloud Function endpoint | `07-pubsub-streaming/labs/lab-04-streaming-dataflow.md` |
| 2 | `bq show --view --authorized_view ...` and `GRANT SELECT ... TO "user:..."` are not valid BigQuery syntax | Authorized views are granted at the **dataset** level (console "Authorize views" or `bq update` access JSON); row/column security via policy tags & row-level access policies | `04-bigquery-advanced/labs/lab-03-authorized-view.md` |
| 3 | `gcloud alpha monitoring policies create` (outdated/broken syntax) | Use `gcloud monitoring` alerts via the JSON alerting policy, or the console | `08-composer-workflow/labs/lab-05-monitor.md` |
| 4 | "CYMNAL Retail" typo in architecture diagram | Corrected to "Cymbal Retail" | Module 11 |
| 5 | Only 5 practice questions shown despite "50" claimed, no explanations | Full 50-question bank **with explanations** + 2 mock exams + case studies | `12-exam-preparation/` |
| 6 | No ML content at all | New Module 13 (BigQuery ML + Vertex AI) | `13-machine-learning/` |
| 7 | Broken/truncated markdown fences and orphaned `bash`/`sql`/`text` labels | All code blocks rebuilt cleanly; every artifact now exists as a real file | whole package |
| 8 | No Windows setup instructions (course was Unix-only) | Windows PowerShell steps included throughout | `00-getting-started/` |
| 9 | No cost control for Composer/Dataproc/streaming (would blow the $300 credits) | Budget/alerts lab + auto-delete + preemptible workers + "stop after lab" notes | Module 1 Lab 5; Modules 5, 6, 8 |
| 10 | Full Looker listed as labbed with free credits (it is an enterprise product) | Labs use free **Looker Studio**; **Looker/LookML** concepts taught as exam content with reference Explore/model files | `09-looker-reporting/` |
| 11 | No Bigtable / Dataplex / Dataform / federated queries / slots content | Added as theory + labs in Modules 3, 4, 6, 10 | various |
| 12 | Streaming lacked watermarks, late data, session windows, exactly-once semantics | Added to Module 5 theory and Lab 3 | `05-dataflow-beam/` |
| 13 | `gcloud data-catalog taxonomies create` / `policy-tags create` don't exist (verified against SDK 573) | Taxonomies + policy tags are created by **importing** a serialized taxonomy file (`taxonomies import`); sample `taxonomy.json` added | `10-security-governance/labs/lab-02-data-catalog-policy-tags.md`, `code/taxonomy.json` |
| 14 | `gcloud dataform repositories create` — no `gcloud dataform` group exists (verified against SDK 573) | Create Dataform repos via console or the Dataform REST API (curl) | `04-bigquery-advanced/labs/lab-06-dataform.md` |

---

## Course map (13 modules + infrastructure + resources)

```
gcp-data-engineer-course/
├── 00-getting-started/            # README, prerequisites, env setup, requirements.txt
├── 01-gcp-overview-setup/         # account, project, IAM, gcloud, service accounts, budgets
├── 02-cloud-storage/              # buckets, classes, lifecycle, versioning, CMEK, transfer
├── 03-bigquery-fundamentals/      # datasets, tables, load, partition/cluster, external tables, slots
├── 04-bigquery-advanced/          # nested/repeated, windows, CTEs, UDFs, views, BI Engine, Dataform
├── 05-dataflow-beam/              # Beam, batch→streaming, windows/triggers, side inputs, templates
├── 06-dataproc-spark/             # clusters, PySpark, Spark SQL, BigQuery connector, workflow templates
├── 07-pubsub-streaming/           # topics/subscriptions, ordering, schemas, DLQ, exactly-once
├── 08-composer-workflow/          # Composer DAGs, Workflows, Eventarc, monitoring
├── 09-looker-reporting/           # Looker Studio + LookML concepts
├── 10-security-governance/        # IAM, policy tags, Data Catalog, VPC-SC, DLP, audit logs
├── 11-end-to-end-project/         # Pub/Sub → Dataflow → BigQuery → Looker Studio (+ dbt)
├── 12-exam-preparation/           # 4-week plan, 50 Q&A, 2 mock exams, case studies, cheat sheets
├── 13-machine-learning/           # BigQuery ML, Vertex AI, batch predictions (NEW)
├── infrastructure/terraform/      # IaC for buckets, BQ, Pub/Sub, SA, IAM, Dataproc, Dataflow
└── resources/                     # shared cheat sheets, architecture diagrams
```

---

## MODULE 00 — Getting Started & Environment

**Labs (see `00-getting-started/`)**
1. Install Python 3.10+ and the Google Cloud SDK on **Windows / macOS / Linux**
2. `gcloud init`, `gcloud auth application-default login`
3. Install Python deps: `pip install -r requirements.txt`
4. Set env vars: `GOOGLE_APPLICATION_CREDENTIALS`, `PROJECT_ID`, `REGION`
5. Cost budget: create a Billing Budget with alerts at 50/75/90/100%

---

## MODULE 01 — GCP Overview & Setup

**Topics:** resource hierarchy, IAM (primitive/predefined/custom), service accounts, gcloud, billing/budgets, free tier.

**Labs (`01-gcp-overview-setup/labs/`)**
1. Create account + project (`gcp-data-engineering-course`)
2. Install gcloud + init (Windows: `choco install googlecloudsdk` or the installer)
3. Create a **service account** with least-privilege roles
4. Enable APIs (BigQuery, Storage, Dataflow, Dataproc, Pub/Sub, Composer, DLP, Data Catalog, Vertex AI, KMS)
5. **Billing budget + alerts** (cost-control lab — required before all other modules)

**Key commands**
```bash
gcloud config set project PROJECT_ID
gcloud iam service-accounts create data-engineer-sa --display-name="Data Engineer SA"
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:data-engineer-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.jobUser"
gcloud iam service-accounts keys create sa-key.json \
  --iam-account="data-engineer-sa@PROJECT_ID.iam.gserviceaccount.com"
export GOOGLE_APPLICATION_CREDENTIALS=$PWD/sa-key.json   # PowerShell: $env:GOOGLE_APPLICATION_CREDENTIALS="$PWD\sa-key.json"
gcloud services enable bigquery.googleapis.com storage.googleapis.com dataflow.googleapis.com \
  dataproc.googleapis.com pubsub.googleapis.com composer.googleapis.com dlp.googleapis.com \
  datacatalog.googleapis.com aiplatform.googleapis.com cloudkms.googleapis.com
```

**Exercise set:** custom IAM role JSON, resource-hierarchy walk-through, "least privilege" scenario questions.

---

## MODULE 02 — Cloud Storage (The Data Lake)

**Topics:** buckets, storage classes (Standard/Nearline/Coldline/Archive), lifecycle, versioning, object holds, retention, uniform vs fine-grained ACLs, CMEK/CSEK/CSE, Storage Transfer Service, Transfer Appliance, requester pays, notifications (Eventarc/Pub/Sub).

**Labs (`02-cloud-storage/labs/` + `code/`)**
1. Create `cymbal-raw-*` and `cymbal-processed-*` buckets with lifecycle + versioning
2. Upload via console, `gsutil`, and `gsutil rsync`; copy public sample data
3. Uniform bucket-level access + IAM bindings
4. **CMEK** encryption via Cloud KMS (key ring + key + bucket + encrypter binding)
5. Storage Transfer Service (HTTP and S3-to-GCS)

**Key commands**
```bash
gsutil mb -l us-central1 gs://cymbal-raw-$(gcloud config get-value project)
gsutil versioning set on gs://cymbal-raw-$(gcloud config get-value project)
gsutil lifecycle set lifecycle-policy.json gs://cymbal-raw-$(gcloud config get-value project)
gsutil uniformbucketlevelaccess set on gs://cymbal-raw-$(gcloud config get-value project)
gsutil iam ch serviceAccount:data-engineer-sa@PROJECT_ID.iam.gserviceaccount.com:objectViewer gs://cymbal-raw-$(gcloud config get-value project)
gcloud kms keyrings create data-keyring --location us-central1
gcloud kms keys create storage-key --location us-central1 --keyring data-keyring --purpose encryption
gsutil mb -k projects/PROJECT_ID/locations/us-central1/keyRings/data-keyring/cryptoKeys/storage-key gs://cymbal-cmek-$(gcloud config get-value project)
gcloud transfer jobs create gs://cymbal-raw-$(gcloud config get-value project) \
  --source-uri="https://storage.googleapis.com/cloud-samples-data/bigquery/sample-transactions/" \
  --schedule-repeats=daily
```

**Exam focus:** when to use Transfer Appliance (large/offline) vs Storage Transfer Service (network); lifecycle to control cost; CMEK vs CSEK vs Google-managed.

---

## MODULE 03 — BigQuery Fundamentals (The Data Warehouse)

**Topics:** BigQuery architecture (Colossus storage, Jupiter network, Borg compute, slot pool), datasets/tables, schema, load (load/streaming/external), partitioning (ingestion-time vs column), clustering, BigLake/external tables, federated queries, on-demand vs flat-rate pricing and **slots**, `INFORMATION_SCHEMA`.

**Labs (`03-bigquery-fundamentals/labs/` + `code/`)**
1. Create `cymbal_warehouse` dataset + partitioned/clustered `taxi_trips` table
2. Load CSV from GCS (`bq load`, SQL `LOAD DATA`, and Python client)
3. Analytical queries with partition pruning + public datasets
4. **External table (BigLake)** over Parquet in GCS + federated query
5. **Slots & cost:** query on-demand, check bytes billed, estimate costs; create a reservation if budget allows

**Key SQL / commands**
```sql
CREATE TABLE cymbal_warehouse.taxi_trips (
  trip_id STRING, vendor_id STRING, pickup_datetime TIMESTAMP, dropoff_datetime TIMESTAMP,
  pickup_location STRING, dropoff_location STRING, trip_distance FLOAT64, fare_amount FLOAT64,
  tip_amount FLOAT64, total_amount FLOAT64, payment_type STRING, passenger_count INT64)
PARTITION BY DATE(pickup_datetime)
CLUSTER BY vendor_id, payment_type;
```
```bash
bq load --source_format=CSV --skip_leading_rows=1 \
  cymbal_warehouse.taxi_trips gs://cymbal-raw-$(gcloud config get-value project)/taxi_trips.csv schema.json
```
```sql
-- BigLake external table over Parquet
CREATE EXTERNAL TABLE cymbal_warehouse.taxi_trips_ext
OPTIONS (format='PARQUET',
         uris=['gs://cymbal-raw-*/taxi_trips/*.parquet']);
```

**Exam focus:** partition pruning + clustering to cut bytes billed; ingestion-time vs column partitioning; external tables & BigLake for data lakes; slot vs on-demand pricing.

---

## MODULE 04 — BigQuery Advanced (Complex Data, Performance & Pipelines)

**Topics:** nested/repeated (STRUCT/ARRAY, UNNEST), window functions, CTEs, UDFs (SQL & JS), **authorized views** (correct pattern), row-level access policies, policy tags, materialized views, BI Engine, Dataform (SQL pipelines as code), cross-region dataset copies, `MERGE`/dbt.

**Labs (`04-bigquery-advanced/labs/` + `code/`)**
1. Query `ga4_obfuscated_sample_ecommerce` nested/repeated `event_params`
2. Window functions + CTEs (running totals, 7-day moving average, ranking)
3. **Authorized view — corrected:** create view, then authorize it on the dataset so analysts with dataset access can use it without table access
4. UDFs (SQL + JS) for currency normalization / timestamp formatting
5. BI Engine reservation + materialized view + **Dataform** repo with a `.sqlx` model

**Authorized view (correct procedure)**
```sql
CREATE VIEW cymbal_warehouse.marketing_trip_view AS
SELECT trip_id, pickup_datetime, pickup_location, dropoff_location, trip_distance, fare_amount
FROM cymbal_warehouse.taxi_trips
WHERE fare_amount > 10;
```
1. Console → BigQuery → dataset `cymbal_warehouse` → **Share → Authorize views** → select `marketing_trip_view`.
2. Grant `roles/bigquery.dataViewer` on the *view's* dataset (or the view) to the marketing group.
3. Marketing never gets access to the underlying `taxi_trips` table.
> The old draft's `bq show --view --authorized_view` and `GRANT SELECT ... TO "user:..."` are **not valid**; use the dataset "Authorize views" mechanism (or the `bq update` JSON access array).

**Row-level access policy (alternative/complement)**
```sql
CREATE ROW ACCESS POLICY marketers_filter
ON cymbal_warehouse.taxi_trips
GRANT TO ("group:marketing@example.com")
FILTER USING (payment_type IN ('CRD','CSH'));
```

**Exam focus:** authorized views & policy tags for column/row security; materialized views for pre-aggregation; Dataform for versioned SQL; window functions over nested data.

---

## MODULE 05 — Dataflow & Apache Beam (Unified Processing)

**Topics:** Beam model (PCollection, PTransform, ParDo, GroupByKey, Combine, side inputs), windows (fixed/sliding/session/global), **triggers (watermark, early/on-time/late)**, `allowed_lateness`, exactly-once vs at-least-once, Dataflow streaming engine, FlexRS, classic vs Flex templates, runner v2.

**Labs (`05-dataflow-beam/labs/` + `code/`)**
1. Run the built-in WordCount template
2. Custom **Python Beam ETL** (read CSV → ParDo clean → BigQuery) on DirectRunner and DataflowRunner
3. **Batch → streaming:** Pub/Sub → fixed 60 s windows → late-data handling with `allowed_lateness` → BigQuery
4. Side inputs (static lookup for enrichment)
5. **Flex template** build + run + cost note (delete job after the lab)

**Core streaming excerpt (`code/streaming_taxi_pipeline.py`)**
```python
windowed = parsed | "Window" >> beam.WindowInto(
    FixedWindows(60),
    trigger=AfterWatermark(early=AfterProcessingTime(30), late=AfterCount(1)),
    allowed_lateness=120,
    accumulation_mode=beam.trigger.AccumulationMode.ACCUMULATING)
```
> **Note:** Dataflow consumes Pub/Sub by **pulling** from a subscription. There is no "push subscription to Dataflow."

**Exam focus:** choosing Dataflow vs Dataproc; FlexRS cost for flexible batch; streaming engine vs batch; triggers/lateness for correctness.

---

## MODULE 06 — Dataproc & Spark (Batch Processing)

**Topics:** cluster types (standard/flex), zones, preemptible VMs, autoscaling, custom images, initialization actions, Cloud Storage + BigQuery connectors, Hive/Spark SQL, workflow templates, `--max-idle` auto-deletion for cost.

**Labs (`06-dataproc-spark/labs/` + `code/`)**
1. Create a cluster **with preemptible workers and auto-delete** (`--max-idle=20m`)
2. PySpark job: GCS → aggregations → BigQuery (BigQuery connector)
3. Spark SQL job
4. BigQuery connector read/write
5. Dataproc **workflow template** (PySpark → Spark SQL) + instantiate
6. Cost control: always delete clusters after labs (`gcloud dataproc clusters delete ...`)

**Key commands**
```bash
gcloud dataproc clusters create taxi-cluster --region=us-central1 \
  --master-machine-type=n1-standard-2 --worker-machine-type=n1-standard-2 \
  --num-workers=2 --num-preemptible-workers=2 --max-idle=20m
gcloud dataproc jobs submit pyspark taxi_analysis.py --cluster=taxi-cluster --region=us-central1 \
  --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar
gcloud dataproc clusters delete taxi-cluster --region=us-central1
```

**Exam focus:** preemptible VMs to cut cost; when Spark/Dataproc is the right tool (legacy, ML feature engineering, complex transforms) vs Dataflow.

---

## MODULE 07 — Pub/Sub & Streaming (Event Ingestion)

**Topics:** topics/subscriptions, pull vs push, message ordering keys, **exactly-once delivery**, schema registry (Avro/Protobuf), dead-letter topics, snapshots & seek, message retention, batching/flow control, idempotency for at-least-once.

**Labs (`07-pubsub-streaming/labs/` + `code/`)**
1. Create topic + pull subscription (with ordering enabled) + schema
2. Python publisher (with ordering keys)
3. Python subscriber (ack/nack) — and a **Cloud Function** push subscriber
4. **Corrected:** Dataflow streaming pipeline **pulls** from the subscription (see Module 5); push is demoed to a Cloud Function
5. DLQ: dead-letter topic, `--max-delivery-attempts=5`, replay via seek/snapshot

**Key commands**
```bash
gcloud pubsub topics create cymbal-orders --message-retention-duration=7d
gcloud pubsub schemas create order-schema --type=AVRO --definition-file=order.avsc
gcloud pubsub topics create cymbal-orders-schema --schema=order-schema --message-encoding=JSON
gcloud pubsub subscriptions create cymbal-orders-sub --topic=cymbal-orders \
  --enable-message-ordering --ack-deadline=60 --enable-exactly-once-delivery
gcloud pubsub topics create cymbal-orders-dlq
gcloud pubsub subscriptions create cymbal-orders-sub-dlq --topic=cymbal-orders \
  --dead-letter-topic=cymbal-orders-dlq --max-delivery-attempts=5
gcloud pubsub snapshots create orders-snapshot --subscription=cymbal-orders-sub
gcloud pubsub subscriptions seek cymbal-orders-sub --time=2024-01-01T00:00:00Z
```

**Exam focus:** exactly-once delivery + idempotent sinks; ordering keys (per-key ordering, not global FIFO); DLQ + snapshots/seek; schema registry for data quality at ingestion.

---

## MODULE 08 — Cloud Composer & Workflows (Orchestration)

**Topics:** Composer/Airflow concepts (DAGs, Operators, hooks, TaskGroups), `DataflowStartFlexTemplateOperator`, `BigQueryInsertJobOperator`, **Cloud Workflows** (serverless YAML orchestration), Cloud Scheduler, Eventarc (event-driven triggers), Cloud Monitoring alerts.

**Labs (`08-composer-workflow/labs/` + `code/`)**
1. Create **small** Composer environment (cost warning: delete after the lab) — or use the Airflow image locally for DAG testing
2. DAG: flex-template Dataflow → BigQuery summary → alert
3. Scheduled BigQuery report DAG
4. **Cloud Workflows** YAML for sequential ETL (function → BigQuery → notification)
5. Monitoring: Cloud Logging for DAG runs + alerting policy (corrected JSON-based syntax)

**Cost note:** a Composer-2 environment costs ~$1–2/day; create, complete the lab, and delete it the same day to stay inside free credits. Prefer local Airflow (via `astro` or Docker) for DAG development.

**Exam focus:** Composer vs Cloud Workflows vs Cloud Scheduler vs Eventarc; DAG dependency modeling; when serverless (Workflows) beats managed Airflow.

---

## MODULE 09 — Looker & Data Studio (Visualization)

**Topics:** Looker Studio (free) for dashboards; **Looker/LookML** concepts for the exam (Explores, Views, Models, dimensions/measures, PDTs); BigQuery BI Engine acceleration; embedding & scheduled delivery.

**Labs (`09-looker-reporting/labs/`)**
1. Connect Looker Studio → BigQuery `cymbal_warehouse`
2. Multi-page report (Executive, Vendor, Geo)
3. Dashboard with date range + vendor + fare controls and cross-filtering
4. Calculated fields (revenue-per-mile, trip category)
5. Share + schedule email + embed `<iframe>`

**Exam-only reference artifacts (`09-looker-reporting/lookml/`)**
- `view_taxi_trips.view.lkml` and `model_taxi.model.lkml` — because the exam tests LookML concepts (Explores/Views/Models, `dimension`/`measure`, `sql:` blocks), which you cannot practice with Looker Studio alone.

**Exam focus:** Looker architecture & LookML terms; BI Engine to accelerate dashboards; connecting Looker Studio vs Looker.

---

## MODULE 10 — Security & Governance

**Topics:** IAM (primitive/predefined/custom, conditions), service accounts & workload identity, **policy tags** (column-level) & taxonomies, row-level access policies, Data Catalog (tag templates), VPC Service Controls, CMEK/CSEK/CSE, **DLP API** (inspect/de-identify), Cloud Audit Logs + export, data retention, Dataplex (governance & lineage).

**Labs (`10-security-governance/labs/` + `code/`)**
1. Custom IAM role JSON (`bigquery.tables.get/list`, `jobs.create`, `storage.objects.*`) + conditions
2. Data Catalog tag template + tag on sensitive columns; **policy tag taxonomy** for column-level access
3. VPC-SC perimeter (dry-run → enforced) around BigQuery/Storage
4. **DLP** inspect + de-identify (redact/mask) PII with the Python client
5. Audit logs → sink to a separate BigQuery dataset → query access logs

**Exam focus:** column-level security = policy tags (not just IAM); VPC-SC for data exfiltration prevention; DLP infoTypes & de-identification transforms; Data Catalog + Dataplex for governance/lineage; CMEK vs CSEK vs CSE.

---

## MODULE 11 — End-to-End Project (Capstone: "Cymbal Retail")

**Architecture**
```
Clickstream Simulator → Pub/Sub → Dataflow (streaming, windows, enrichment) → BigQuery
                                                                              ├─ Bronze: clickstream_raw
                                                                              ├─ Silver: dbt models (stg_*)
                                                                              └─ Gold: fct_daily_sales
Cloud Composer (hourly DAG: validate → dbt → backfill) ───────────────────────┘
Looker Studio dashboard on gold tables  (BI Engine for acceleration)
Cloud Storage: staging/temp + archival of raw events
```

**Deliverables (`11-end-to-end-project/`)**
- `code/simulator.py` — publishes simulated clickstream to Pub/Sub
- `code/streaming_pipeline.py` — Beam pipeline: parse → enrich → Bronze + windowed Gold writes
- `dbt/` — dbt project (`profiles.yml`, `stg_events.sql`, `fct_daily_sales.sql`, `schema.yml`)
- `code/dags/end_to_end_dag.py` — Composer DAG (validation → dbt → backfill → alert)
- `dashboard/` — Looker Studio layout & metrics guide
- `architecture/architecture.md` + diagram (typo corrected)

---

## MODULE 12 — Exam Preparation

Files in `12-exam-preparation/`:
- `study-plan.md` — 4-week plan (week-by-week mapping to modules + mock schedule)
- `practice-questions-50.md` — **50 questions with detailed answer explanations** (replaces the 5-question stub)
- `mock-exam-1.md` & `mock-exam-2.md` — two full-length, timed practice exams (25 Qs each)
- `case-studies.md` — exam-style case studies + questions
- `cheat-sheets.md` — service-vs-service decision tables ("when to use X")
- `glossary.md` — 100+ key terms
- `exam-tips.md` — question strategy, guessing strategy, time management, "Google way" thinking

---

## MODULE 13 — Machine Learning (NEW, closes the 15–20% gap)

**Topics:** BigQuery ML (`CREATE MODEL`, `ML.PREDICT`, `ML.TRAINING_INFO`, `ML.EVALUATE`, `ML.EXPLAIN_PREDICT`), linear/logistic regression, XGBoost, k-means, time-series (ARIMA_PLUS), matrix factorization; Vertex AI (datasets, training, endpoints, batch prediction, AutoML); model lifecycle & versioning; features (Vertex AI Feature Store); ML on streaming vs batch; when to use BQML vs Vertex AI vs Dataproc MLlib.

**Labs (`13-machine-learning/labs/` + `code/`)**
1. **BQML linear regression** on taxi trips (fare ~ distance + duration), `ML.EVALUATE`, `ML.PREDICT`
2. **BQML logistic regression** (churn) + `ML.ROC_CURVE`, model explainability
3. **BQML k-means** clustering (customer segments) + `ML.EXPLAIN_PREDICT`
4. **Vertex AI:** train a small model, deploy to an endpoint, run batch prediction
5. **ML lifecycle & cost:** model versioning, feature store overview, cost-control (delete endpoints after lab)

**Sample (`13-machine-learning/code/bqml_fare_model.sql`)**
```sql
CREATE OR REPLACE MODEL cymbal_warehouse.fare_model
OPTIONS (model_type='LINEAR_REG', input_label_cols=['fare_amount']) AS
SELECT
  trip_distance, passenger_count, vendor_id,
  TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, MINUTE) AS duration_min,
  fare_amount
FROM cymbal_warehouse.taxi_trips
WHERE fare_amount > 0;
```
```sql
SELECT * FROM ML.PREDICT(MODEL cymbal_warehouse.fare_model,
  (SELECT * FROM cymbal_warehouse.taxi_trips WHERE fare_amount > 0 LIMIT 100));
```

**Exam focus:** when to use BQML (in-warehouse, no data movement) vs Vertex AI (custom/deep learning, full MLOps) vs Dataproc MLlib (large-scale custom feature engineering); batch prediction vs online endpoints; model monitoring.

---

## MODULE 14+ — Course Production Checklist

- [ ] All labs re-run against **current** APIs (check deprecations at publication time: e.g., Beam `ReadFromPubSub` vs `ReadFromPubSubWithAttributes`)
- [ ] 50 Q&A + 2 mocks reviewed against official sample questions
- [ ] Video scripts drafted per module (see `resources/recording-guide.md`)
- [ ] Starter branch (labs empty) vs `solutions` branch (this package)
- [ ] Terraform applied/destroyed in a throwaway project
- [ ] Landing page: title, target audience, curriculum, promo video outline

---

## Quick start for students

```bash
git clone <course-repo> && cd gcp-data-engineer-course
# Windows PowerShell
$env:PROJECT_ID="your-project-id"
$env:GOOGLE_APPLICATION_CREDENTIALS="$PWD\sa-key.json"
gcloud config set project $env:PROJECT_ID
python -m venv .venv && .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd infrastructure/terraform
terraform init && terraform apply -var="project_id=$env:PROJECT_ID"
```
