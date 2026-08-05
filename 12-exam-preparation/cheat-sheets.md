# GCP Data Engineer — Cheat Sheets

## Storage & Warehousing

| Service | Best for | Key facts |
|---|---|---|
| Cloud Storage | Data lake, unstructured | Classes Standard/Nearline/Coldline/Archive; versioning; lifecycle |
| BigQuery | Data warehouse / OLAP | Partition+cluster; on-demand vs reservations; BI Engine; BQML |
| Bigtable | NoSQL, low-latency | Row keys = hot-spot risk; wide column; ~10ms reads |
| Cloud SQL | Managed MySQL/Postgres/SQL Server | Regionally managed; HA read replicas |
| Spanner | Global strong-consistency relational | Horizontal scale + SQL + strong consistency |
| Firestore | App data, realtime | Serverless NoSQL document DB |
| Memorystore | Redis/Memcached cache | For caching, sessions |

## Processing

| Service | Best for | Notes |
|---|---|---|
| Dataflow | Unified stream/batch (Beam) | Windows/triggers; FlexRS; streaming engine; templates |
| Dataproc | Managed Spark/Hadoop/Hive | Preemptible workers; workflow templates; `gs://` native |
| Pub/Sub | Async messaging / ingestion | Pull vs push; exactly-once; ordering keys; DLQ; schemas |
| Composer | Orchestration (Airflow) | DAGs, operators, retries, backfills |
| Cloud Workflows | Serverless linear orchestration | YAML steps; HTTP/Google APIs |
| Cloud Scheduler | Cron | Trigger one job on schedule |
| Eventarc | Event-driven triggers | GCS/Pub/Sub events → Cloud Run/Workflows |
| Cloud Functions | Lightweight serverless | Pub/Sub push endpoint (correct push pattern) |
| Dataflow SQL | Streaming SQL (ZetaSQL) | SQL-only streaming pipelines |

## Machine Learning

| Need | Tool |
|---|---|
| Train where data lives (SQL) | BigQuery ML |
| Custom/deep learning, MLOps | Vertex AI |
| Huge custom feature engineering on Spark | Dataproc MLlib |
| Serve low-latency | Vertex AI online endpoint |
| Offline large-volume scoring | Vertex AI batch prediction |
| Detect drift/skew | Vertex AI Model Monitoring |

## Governance & Security

| Concern | Tool |
|---|---|
| Column-level security | BigQuery **policy tags** |
| Row-level security | `CREATE ROW ACCESS POLICY` |
| Share subset w/o table access | **Authorized views** |
| Metadata discovery/tagging | Data Catalog |
| Governance, lineage, quality | Dataplex |
| PII inspect/de-identify | Cloud DLP |
| Prevent exfiltration | VPC Service Controls |
| Keys (you manage) | Cloud KMS (CMEK) |
| Audit trail | Cloud Audit Logs + sinks |
| Access rules | IAM (primitive/predefined/custom + conditions) |

## "When to use X vs Y" one-liners

- **BigQuery vs Bigtable:** analytics/aggregations → BigQuery; point lookups/latency → Bigtable.
- **Dataflow vs Dataproc:** Beam/unified stream+batch → Dataflow; existing Spark/Hive, ML feature engineering → Dataproc.
- **Composer vs Workflows:** complex dependencies/backfills → Composer; simple linear serverless → Workflows.
- **Transfer Appliance vs STS:** big + slow network → Appliance; periodic/online → STS.
- **BQML vs Vertex:** data in BQ + SQL → BQML; custom/deep learning → Vertex.
- **CMEK vs CSEK:** CMEK (keys in KMS) is preferred; CSEK = you supply raw keys (legacy).
- **Push vs Pull:** HTTP endpoint → push (Cloud Function/Run); Dataflow/workers → pull.
- **On-demand vs flat-rate:** unpredictable usage → on-demand; steady heavy → flat-rate.
- **Materialized view vs view:** pre-compute for speed → materialized; simple passthrough → view.
- **Policy tags vs authorized views:** hide a column from everyone → policy tag; share a filtered subset → authorized view.

## BigQuery cost levers
1. Partition + cluster. 2. Select only needed columns. 3. Use Parquet not CSV.
4. Materialized views for repeated aggregates. 5. Wildcard + `_TABLE_SUFFIX`.
6. Dry-run to preview cost. 7. Table/dataset expiration. 8. BI Engine for hot dashboards.
