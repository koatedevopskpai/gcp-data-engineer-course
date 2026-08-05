# Mock Exam 2 (timed: 60 minutes, 25 questions)

**1.** To query CSV files in GCS without loading them, you create:
- A) An external table
- B) A materialized view
- C) A schema
- D) A Pub/Sub topic

**2.** Which BigQuery feature reduces bytes billed for queries filtered on
`DATE(event_time)`?
- A) Clustering only
- B) Partitioning by `DATE(event_time)`
- C) BI Engine
- D) Materialized views (alone)

**3.** A marketing user should see only rows where `region='US'`. Best approach?
- A) Authorized view with `WHERE region='US'`
- B) Policy tags
- C) A new user per region
- D) Object versioning

**4.** Which service provides managed Apache Spark?
- A) Dataflow
- B) Dataproc
- C) Composer
- D) Vertex AI

**5.** Pub/Sub messages that fail processing 5 times are routed to:
- A) The DLQ topic
- B) BigQuery automatically
- C) Cloud Storage
- D) The publisher

**6.** Which Beam trigger emits partial results before the watermark?
- A) Late trigger
- B) Early trigger (AfterProcessingTime)
- C) On-time trigger only
- D) No trigger

**7.** The most reliable way to monitor a Composer DAG failure:
- A) Cloud Monitoring alert on DAG/task failed metrics
- B) Email from users
- C) Checking once a week
- D) A cron job

**8.** BQML `ML.EXPLAIN_PREDICT` shows:
- A) Feature attributions for a prediction
- B) The training loss
- C) The schema
- D) Query cost

**9.** Which sink is best to ingest ~50,000 events/sec into BigQuery with
dedup?
- A) BigQuery Storage Write API (streaming)
- B) Daily CSV load
- C) Looker Studio
- D) Cloud Functions only

**10.** A table is queried frequently by `vendor_id` AND `payment_type` filters
within a date partition. Design:
- A) Partition by vendor, cluster by date
- B) Partition by date, cluster by vendor_id, payment_type
- C) No partitioning
- D) Partition by payment_type

**11.** Vertex AI Feature Store is used to:
- A) Store/serve ML features consistently
- B) Store raw logs
- C) Run SQL
- D) Serve dashboards

**12.** Which tool migrates data from AWS S3 to GCS periodically?
- A) Transfer Appliance
- B) Storage Transfer Service
- C) gsutil cp only
- D) Cloud Dataflow

**13.** To ensure a workflow reacts to a new object in GCS in <1 minute:
- A) Eventarc + Cloud Run/Workflows
- B) Cloud Scheduler hourly
- C) BigQuery scheduled query
- D) Manual copy

**14.** Which is the CORRECT statement about Dataflow side inputs?
- A) They change per element
- B) They are read once and broadcast
- C) They cannot be used with streaming
- D) They are a storage service

**15.** DLP `crypto_deterministic_config` produces:
- A) Reversible, stable pseudonyms
- B) Irreversible random values
- C) Base64
- D) Hash of the whole column

**16.** Data catalog tag templates vs policy tags:
- A) Tags = metadata; policy tags = access control
- B) They are identical
- C) Policy tags are metadata
- D) Neither affects access

**17.** Which option reduces BigQuery on-demand cost for exploratory queries?
- A) Add `LIMIT` only
- B) Query fewer columns + partition filters + dry-run checks
- C) Use more clusters
- D) Enable VPC-SC

**18.** A streaming job must group a user's actions within 30-min idle gaps:
- A) FixedWindows(1800)
- B) SessionWindows(1800)
- C) SlidingWindows(1800, 60)
- D) GlobalWindow

**19.** To deploy the same parameterized Beam pipeline in production, use:
- A) A Flex Template
- B) A one-off script
- C) Dataproc cluster
- D) Cloud SQL

**20.** `ML.PREDICT(MODEL m, (SELECT ...))`:
- A) Trains m
- B) Runs inference
- C) Evaluates m
- D) Drops m

**21.** Which audit log type is always enabled and records config changes?
- A) Admin activity
- B) Data access
- C) System event
- D) Policy denied

**22.** A retention period on GCS objects is enforced via:
- A) IAM only
- B) Bucket retention policy
- C) Lifecycle delete
- D) Versioning only

**23.** Which service provides column-level masking with policy tags in BQ?
- A) BigQuery policy tags
- B) Dataflow
- C) Looker
- D) Composer

**24.** The exam "Google way" answer for "which fully managed SQL warehouse?" is:
- A) BigQuery
- B) Dataproc Hive
- C) Spark SQL on VMs
- D) Cloud Functions

**25.** Before the exam, the single highest-value preparation activity is:
- A) Timed mock exams + reviewing wrong answers
- B) Reading only
- C) Watching videos without labs
- D) Memorizing IP addresses

---

## Key

1-A, 2-B, 3-A, 4-B, 5-A, 6-B, 7-A, 8-A, 9-A, 10-B, 11-A, 12-B, 13-A, 14-B,
15-A, 16-A, 17-B, 18-B, 19-A, 20-B, 21-A, 22-B, 23-A, 24-A, 25-A.

Target: ≥18/25. For each miss, note the domain and re-run that module's labs.
