# Mock Exam 1 (timed: 60 minutes, 25 questions)

Instructions: answer all questions, then check the key. Use this to find weak
domains, then revisit the corresponding module labs.

**1.** Which BigQuery pricing model is best for steady, predictable heavy query
workloads?
- A) On-demand
- B) Flat-rate (reservations)
- C) Per-slot billing
- D) Free tier

**2.** A streaming pipeline must aggregate page views per minute and tolerate 2
minutes of late data. Which Beam config is correct?
- A) FixedWindows(60) with `allowed_lateness=120`
- B) GlobalWindow
- C) Session windows only
- D) No windowing

**3.** Which IAM role allows reading objects in a bucket without listing buckets?
- A) `roles/storage.objectViewer`
- B) `roles/storage.admin`
- C) `roles/viewer`
- D) `roles/storage.bucketAdmin`

**4.** You need to detect credit-card numbers in customer text before loading to
BigQuery. Which service?
- A) Cloud DLP
- B) Data Catalog
- C) Cloud KMS
- D) Cloud Audit Logs

**5.** A Dataproc cluster with spot workers lost two workers; the job still
completed. This is possible because Spark:
- A) Requires all workers always
- B) Is fault-tolerant and re-runs lost tasks
- C) Uses BigQuery only
- D) Never loses state

**6.** Which window is best for grouping a user's actions into "sessions" based
on idle gaps?
- A) Fixed
- B) Sliding
- C) Session
- D) Global

**7.** BigQuery native table vs BigLake external table — which statement is true?
- A) Native tables cannot be queried
- B) BigLake queries Parquet/CSV in GCS with BigQuery security
- C) External tables support clustering
- D) BigLake requires copying data in

**8.** Composer is best described as:
- A) A serverless function runtime
- B) Managed Apache Airflow
- C) A data warehouse
- D) A messaging bus

**9.** Which query finds top 3 vendors by revenue per day?
- A) Window function with RANK partitioned by day
- B) GROUP BY vendor
- C) SELECT DISTINCT
- D) A self-join without window

**10.** Pub/Sub **ordering keys** guarantee:
- A) Global FIFO across the whole topic
- B) Per-key ordering
- C) Exactly-once publish
- D) Message compression

**11.** A batch job must process a year of Parquet files. Best single framework
choice for cost + simplicity?
- A) Dataflow (batch Beam)
- B) Always a streaming pipeline
- C) Cloud Functions
- D) Cloud SQL

**12.** What does `bq mk --time_partitioning_field=ts` do?
- A) Creates a clustered table
- B) Partitions by the `ts` column
- C) Enables BI Engine
- D) Sets a table expiration

**13.** Vertex AI **batch prediction** vs **online endpoint**:
- A) Batch is for low-latency serving
- B) Online endpoints scale to zero cost
- C) Batch is offline and cheaper for large volumes
- D) They are identical

**14.** Which log sink destination is best for 5-year audit archival?
- A) Cloud Storage (Archive class)
- B) A single BigQuery partition
- C) Pub/Sub topic only
- D) Local disk

**15.** `CREATE ROW ACCESS POLICY` is used for:
- A) Column-level masking
- B) Row-level filtering
- C) Table partitioning
- D) Encryption

**16.** A malicious insider could exfiltrate data to an external bucket. Which
control mitigates?
- A) VPC Service Controls
- B) Object versioning
- C) BigQuery BI Engine
- D) Cloud Composer

**17.** You need to share a subset of a BigQuery table with a vendor, hiding
`customer_email`. Best approach?
- A) Grant them `bigquery.dataViewer` on the table
- B) An authorized view that omits the column
- C) A public dataset
- D) Export to a shared spreadsheet

**18.** Which Beam transform sums per key?
- A) ParDo
- B) CombinePerKey
- C) Flatten
- D) CoGroupByKey

**19.** Cloud Workflows is most appropriate for:
- A) Complex DAGs with retries and backfills
- B) Simple linear serverless automation
- C) SQL warehousing
- D) Real-time messaging

**20.** BQML model trained with `model_type='BOOSTED_TREE_CLASSIFIER'` is used
for:
- A) Regression
- B) Classification
- C) Clustering
- D) Forecasting

**21.** Which is NOT a Cloud Storage storage class?
- A) Standard
- B) Nearline
- C) Glacier
- D) Archive

**22.** A GCS object with a retention policy is deleted. What happens?
- A) Deleted immediately
- B) Deletion blocked until retention expires
- C) Versioned automatically
- D) Empties the bucket

**23.** Data quality: a dbt model must fail if `event_id` has duplicates. Use:
- A) `tests: - unique` in schema.yml
- B) A WHERE clause
- C) Looker Studio
- D) Pub/Sub schema

**24.** Which service scans data for policy-compliance metadata (Dataplex)?
- A) Data Catalog alone
- B) Dataplex (governance, quality, lineage)
- C) Cloud DLP
- D) Cloud Logging

**25.** The most cost-effective way to stop a Dataflow streaming job when a lab
is over:
- A) Leave it running
- B) Cancel the job via console/`gcloud dataflow jobs cancel`
- C) Delete the project
- D) Pause Pub/Sub

---

## Key

1-B, 2-A, 3-A, 4-A, 5-B, 6-C, 7-B, 8-B, 9-A, 10-B, 11-A, 12-B, 13-C, 14-A,
15-B, 16-A, 17-B, 18-B, 19-B, 20-B, 21-C (Glacier is AWS), 22-B, 23-A, 24-B, 25-B.

**Domain mapping:** 1,11,12,21 → Design/Storage · 2,5,6,9,10,13,16,18,22,25 →
Build & Operationalize · 15,20 → ML · 3,4,7,8,14,17,19,23,24 → Quality/Governance.

Score /25 → target ≥18 (72%) to feel exam-ready.
