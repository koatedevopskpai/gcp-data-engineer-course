# 50 Practice Questions (with detailed explanations)

> Covers all four exam domains. Answers are in blocks after each question set —
> first answer all 50, then reveal.

## Questions 1–10 (Design: 20–25%)

**Q1.** You must migrate 100 TB of on-premises data to Cloud Storage. The WAN is
limited to 50 Mbps. Which approach is most appropriate?
- A) `gsutil cp`
- B) Storage Transfer Service
- C) Transfer Appliance
- D) Cloud Storage FUSE

**Q2.** You need column-level security in BigQuery so only finance can read the
`salary` column. What should you use?
- A) Authorized views only
- B) Policy tags (column-level access)
- C) A new table without the column
- D) IAM roles on the table

**Q3.** Which is the primary benefit of Dataflow **FlexRS**?
- A) Lower streaming latency
- B) Cost savings for batch workloads with flexible start times
- C) Higher throughput
- D) Better security

**Q4.** How do you achieve **exactly-once** message processing end-to-end?
- A) Enable at-least-once on the topic
- B) Use a subscription with exactly-once delivery + an idempotent sink
- C) Use only push subscriptions
- D) Enable snapshots

**Q5.** Which BigQuery feature best accelerates repeated dashboard queries?
- A) Partitioning
- B) Clustering
- C) BI Engine
- D) Named datasets

**Q6.** A retail company runs daily batch ETL with occasional streaming. They
want a single processing framework. Which service?
- A) Cloud Dataproc
- B) Cloud Dataflow
- C) Cloud Composer
- D) Cloud Functions

**Q7.** Which storage class is cheapest for data read once a year?
- A) Standard
- B) Nearline
- C) Coldline
- D) Archive

**Q8.** You need low-latency (<10 ms) key-value access for user profiles at scale.
- A) BigQuery
- B) Cloud SQL
- C) Cloud Bigtable
- D) Cloud Spanner

**Q9.** Which model is best when you need global, strongly consistent relational
data with a single logical database?
- A) Bigtable
- B) Spanner
- C) Firestore
- D) Cloud SQL

**Q10.** Streaming sensor data arrives out of order with delays up to 5 minutes.
Choose the Dataflow design.
- A) Fixed windows, no allowed lateness
- B) Session windows, `allowed_lateness` >= 5 min
- C) Global window only
- D) Sliding windows with a 1-second slide

## Questions 11–20 (Build & Operationalize: 30–35%)

**Q11.** In Apache Beam, which transform applies a function element-wise?
- A) GroupByKey
- B) Combine
- C) ParDo
- D) Window

**Q12.** Dataflow can read a Pub/Sub topic via:
- A) A push subscription pointed at the Dataflow job
- B) A pull subscription on a topic
- C) Direct socket connection
- D) Cloud Scheduler

**Q13.** A job must react when a new file lands in Cloud Storage. Best trigger?
- A) Poll every minute with a cron
- B) Pub/Sub notification → Eventarc → workflow
- C) BigQuery scheduled query
- D) Cloud Monitoring alert

**Q14.** You want the cheapest Dataproc worker option for fault-tolerant Spark.
- A) Preemptible/spot VMs
- B) Standard worker VMs
- C) A single master with 8 vCPUs
- D) GPUs

**Q15.** Which transforms data as SQL in a streaming pipeline using Dataflow?
- A) Dataflow SQL (ZetaSQL)
- B) PySpark
- C) LookML
- D) Cloud Workflows

**Q16.** BigQuery loads ~1 PB of Parquet daily from GCS. Cheapest, fastest path?
- A) Load via single `bq load` with CSV
- B) Streaming insert every row
- C) Bulk load of Parquet files (job), partitioned tables
- D) Re-insert via App Engine

**Q17.** Your pipeline must write the same Pub/Sub message stream to BigQuery
AND GCS. How many Dataflow jobs?
- A) Two separate pipelines reading the same subscription
- B) One pipeline with two sinks (Branched PCollection)
- C) One pipeline per consumer
- D) Write to GCS only, then copy

**Q18.** Which tool best orchestrates an ETL with retries, backfills, and
dependent Spark + Dataflow steps?
- A) Cloud Workflows
- B) Cloud Composer (Airflow)
- C) Cloud Scheduler
- D) Eventarc

**Q19.** A Beam job keeps failing on malformed JSON messages. Best practice?
- A) Let the job crash and restart
- B) Route bad messages to a dead-letter collection and continue
- C) Drop all messages
- D) Increase window size

**Q20.** You need a parameterized pipeline that analysts can run from the
console without code. Best approach?
- A) Cloud Functions
- B) Dataflow Flex Template
- C) Dataproc cluster
- D) Composer DAG only

## Questions 21–30 (Build & Operationalize — continue)

**Q21.** Which sink provides the strongest deduplication for streaming inserts?
- A) GCS text files
- B) BigQuery with a primary-key–based dedup table
- C) Pub/Sub topic
- D) Firestore

**Q22.** Dataproc reads GCS natively via:
- A) The Cloud Storage connector (gs://)
- B) FUSE only
- C) A separate ETL
- D) HDFS replication

**Q23.** Your query scans 2 TB but a partition filter would scan 10 GB. What
does the filter save?
- A) Storage cost
- B) Query cost (bytes billed) and time
- C) Nothing
- D) Egress

**Q24.** Composer environments and Dataflow streaming jobs are the biggest
course costs. Which control does NOT help?
- A) Preemptible workers
- B) `--max-idle` auto-delete
- C) Deleting resources after each lab
- D) Always running a large cluster

**Q25.** A pipeline needs a lookup table of 100 MB for enrichment. Which Beam
pattern?
- A) Join with a giant PCollection
- B) Side input (`AsDict`)
- C) A second window
- D) GroupByKey on the whole data

**Q26.** You must replay messages from 2 days ago for reprocessing. Use:
- A) Publish again manually
- B) Seek the subscription to a snapshot/time
- C) Delete and recreate the topic
- D) Increase retention

**Q27.** Which Pub/Sub feature enforces the message structure at publish time?
- A) DLQ
- B) Schema registry
- C) Ordering keys
- D) Snapshots

**Q28.** GA4 export lands as `events_YYYYMMDD`. Querying a month should use:
- A) `WHERE _PARTITIONTIME = ...`
- B) Wildcard `events_*` + `_TABLE_SUFFIX` filter
- C) `SELECT * FROM events`
- D) A view per day

**Q29.** Which query construct computes a running total without a self-join?
- A) GROUP BY
- B) Window function (OVER)
- C) ARRAY_AGG
- D) UNION ALL

**Q30.** A Dataflow job is underutilized and expensive. Best lever?
- A) Increase `max_num_workers`
- B) Right-size `max_num_workers` and use autoscaling
- C) Add more sinks
- D) Use a bigger machine type always

## Questions 31–40 (ML Models: 15–20%)

**Q31.** Train a regression model where data already lives in BigQuery. Cheapest
no-movement option?
- A) Vertex AI custom training
- B) BigQuery ML (`CREATE MODEL`)
- C) Dataproc MLlib
- D) Vertex AI AutoML

**Q32.** In BQML, which option names the target variable?
- A) `model_type`
- B) `input_label_cols`
- C) `data_split_method`
- D) `standardize_features`

**Q33.** BQML classification metrics available:
- A) `ML.EVALUATE` only
- B) `ML.ROC_CURVE`, `ML.CONFUSION_MATRIX`, `ML.EVALUATE`
- C) `ML.TRAINING_INFO` only
- D) `ML.FORECAST`

**Q34.** Which BQML algorithm is for time-series forecasting?
- A) KMEANS
- B) ARIMA_PLUS
- C) MATRIX_FACTORIZATION
- D) BOOSTED_TREE_CLASSIFIER

**Q35.** A model must serve predictions at <100 ms. Choose:
- A) Batch prediction
- B) Online Vertex AI endpoint
- C) Dataflow pipeline
- D) Looker Studio

**Q36.** To segment customers with no labels, use BQML:
- A) LINEAR_REG
- B) KMEANS
- C) LOGISTIC_REG
- D) ARIMA_PLUS

**Q37.** Detecting that serving data differs from training data is:
- A) Overfitting
- B) Data drift / skew
- C) Regularization
- D) Cold start

**Q38.** Which is best for a custom deep-learning vision model?
- A) BQML
- B) Vertex AI custom training
- C) Cloud SQL
- D) Dataproc Hive

**Q39.** What does `ML.PREDICT` do?
- A) Trains a model
- B) Generates predictions for a given dataset
- C) Evaluates accuracy
- D) Deletes a model

**Q40.** Vertex AI Model Monitoring is used for:
- A) Billing
- B) Skew and drift detection on features
- C) Query optimization
- D) Data masking

## Questions 41–50 (Quality & Governance: 15–20%)

**Q41.** Which grants a user the ability to query but not see a sensitive column?
- A) Table-level IAM + policy tag on the column
- B) `roles/owner`
- C) Making the table public
- D) A backup copy

**Q42.** DLP transforms that allow reversing to the original value are:
- A) Redaction only
- B) Crypto-deterministic (with key) / reversible encryption
- C) Masking
- D) Nothing is reversible

**Q43.** To prevent data exfiltration from BigQuery/Storage, use:
- A) A firewall rule only
- B) VPC Service Controls perimeter
- C) IAM on every user
- D) Object versioning

**Q44.** Which audit log type records reads of data and is off by default?
- A) Admin activity
- B) Data access
- C) System event
- D) Policy denied

**Q45.** Exporting audit logs for 400+ day retention is best done with:
- A) A log sink to BigQuery/GCS
- B) A Cloud Function reading logs
- C) `gcloud logging read`
- D) Screenshots

**Q46.** What is Data Catalog used for?
- A) Storing data
- B) Discovering, tagging, and governing data assets
- C) Processing data
- D) Serving models

**Q47.** CMEK means:
- A) Google owns and rotates keys
- B) You manage keys in Cloud KMS
- C) You supply raw key material (deprecated CSEK)
- D) No encryption

**Q48.** Which service provides a fully managed data-governance and lineage layer
(Dataplex)?
- A) Looker
- B) Dataplex
- C) Dataflow
- D) Pub/Sub

**Q49.** A daily aggregation must not double-count when the job reruns. Which
pattern?
- A) Append all rows
- B) Idempotent `MERGE`/`CREATE OR REPLACE` on a date key
- C) Insert with randomness
- D) Never rerun

**Q50.** For data-quality tests on dbt models, you define:
- A) Models in `.sqlx`
- B) `tests:` blocks (not_null, unique) in `schema.yml`
- C) Lifecycle rules
- D) IAM bindings

---

## Answer Key & Explanations

**Q1 → C.** Transfer Appliance ships physical storage for bulk offline migration
when bandwidth is limited. `gsutil` and STS still need the network; FUSE is for
mounting, not migration.

**Q2 → B.** Policy tags enforce column-level access in BigQuery; authorized views
share subsets but don't hide individual columns from table readers.

**Q3 → B.** FlexRS gives discounts for flexible, non-urgent batch workloads (it
can wait for capacity). It is batch-only.

**Q4 → B.** Exactly-once requires exactly-once delivery on the subscription AND
an idempotent downstream sink (e.g., dedup by primary key). Push is a delivery
mode, not a guarantee.

**Q5 → C.** BI Engine caches hot BigQuery data in memory for sub-second dashboard
latency. Partitioning/clustering reduce bytes scanned but don't cache.

**Q6 → B.** Dataflow (Apache Beam) unifies batch and streaming in one framework.

**Q7 → D.** Archive has the lowest storage cost but the highest access costs and
365-day minimum — for rarely accessed/retained data.

**Q8 → C.** Bigtable = low-latency, high-throughput NoSQL, ideal for
time-series/user profiles. Cloud SQL/Spanner are relational; BigQuery is OLAP.

**Q9 → B.** Cloud Spanner = globally distributed relational DB with strong
consistency. Bigtable is NoSQL.

**Q10 → B.** Session windows group bursts; `allowed_lateness` handles out-of-order
data within 5 minutes. Fixed windows would split sessions; global can't aggregate
in time.

**Q11 → C.** ParDo applies a DoFn to each element (map/flatMap). GroupByKey groups,
Combine aggregates, Window assigns event-time windows.

**Q12 → B.** Dataflow pulls from a Pub/Sub subscription. There is no push-into-
Dataflow; push endpoints are HTTP services (Cloud Functions/Run).

**Q13 → B.** GCS object-change notification → Pub/Sub → Eventarc triggers a
Workflow/Cloud Run — event-driven and serverless.

**Q14 → A.** Preemptible/spot workers are ~60–80% cheaper and fine for
fault-tolerant Spark jobs.

**Q15 → A.** Dataflow SQL (ZetaSQL) writes streaming SQL pipelines without Beam
code.

**Q16 → C.** Bulk-load Parquet in jobs (not streaming inserts), partition by date.
CSV is slower/bigger; streaming inserts are for low-latency, not bulk.

**Q17 → B.** One pipeline, branch the PCollection to two sinks. Two consumers
reading the same subscription would split messages.

**Q18 → B.** Airflow (Composer) is built for complex dependencies, retries, and
backfills. Workflows is for simpler serverless sequences.

**Q19 → B.** Route invalid messages to a dead-letter sink; the job continues.
This is the resilient-streaming pattern.

**Q20 → B.** Flex Templates let non-engineers run parameterized pipelines from the
console with no code.

**Q21 → B.** BigQuery streaming dedup by primary key (Storage Write API) provides
strong once-only guarantees. GCS files have no dedup.

**Q22 → A.** Dataproc reads `gs://` natively via the Cloud Storage connector.

**Q23 → B.** Query cost is per-byte-scanned; partition pruning cuts bytes billed
and runtime. Storage cost is unaffected.

**Q24 → D.** Always-running large clusters is the anti-pattern. The others
control cost.

**Q25 → B.** A 100 MB lookup as `AsDict` side input is broadcast to workers —
the textbook enrichment pattern.

**Q26 → B.** Snapshots/seek rewind a subscription to a point in time or snapshot
to reprocess.

**Q27 → B.** Schema registry (Avro/Protobuf) validates messages at publish.

**Q28 → B.** `events_*` with `_TABLE_SUFFIX BETWEEN` restricts partitions across
a month — the GA4 standard.

**Q29 → B.** `SUM(x) OVER (ORDER BY ...)` computes running totals without a join.

**Q30 → B.** Autoscaling + a sane `max_num_workers` matches capacity to load.
More workers doesn't help idle jobs.

**Q31 → B.** BQML trains where data lives, no movement, free tier applies.

**Q32 → B.** `input_label_cols` names the label column.

**Q33 → B.** BQML offers ROC curve, confusion matrix, and evaluation functions.

**Q34 → B.** ARIMA_PLUS forecasts time series (horizon, confidence).

**Q35 → B.** Online endpoints serve low-latency requests; batch is offline.

**Q36 → B.** K-means is unsupervised clustering.

**Q37 → B.** Serving/training distribution mismatch = skew/drift; Model Monitoring
detects it.

**Q38 → B.** Vertex AI custom training supports arbitrary frameworks (TensorFlow,
PyTorch) for deep learning.

**Q39 → B.** `ML.PREDICT` runs inference on a dataset.

**Q40 → B.** Vertex AI Model Monitoring watches feature skew/drift.

**Q41 → A.** Policy tags hide columns; IAM controls access; `owner` is too broad.

**Q42 → B.** Crypto-deterministic transforms are reversible with the key.

**Q43 → B.** VPC-SC builds a data perimeter preventing exfiltration across
services.

**Q44 → B.** Data-access logs are disabled by default because of cost/privacy.

**Q45 → A.** Log sinks stream to BigQuery (queryable) or GCS (archival).

**Q46 → B.** Data Catalog = metadata discovery + tagging + governance.

**Q47 → B.** CMEK = keys managed by you in Cloud KMS.

**Q48 → B.** Dataplex = centralized data governance, quality, and lineage.

**Q49 → B.** Idempotent writes (MERGE/partition overwrite) prevent double counts.

**Q50 → B.** dbt tests live in `schema.yml` (`not_null`, `unique`, custom).
