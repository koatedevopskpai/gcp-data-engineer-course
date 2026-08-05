# Glossary (exam terms)

## A–C
- **ADC** — Application Default Credentials; used by SDKs locally.
- **Authorized view** — view granted access to its source dataset; users query the
  view, not the table.
- **BigLake** — external tables over GCS with BigQuery security/governance.
- **BI Engine** — in-memory acceleration for BigQuery dashboard queries.
- **BQML** — BigQuery ML: train models with SQL inside BigQuery.
- **Catchup** (Airflow) — whether to run missed schedules when DAG enabled.
- **Clustering** — physical ordering of blocks within partitions for cheaper scans.
- **CMEK** — customer-managed encryption keys (in Cloud KMS).
- **CSEK** — customer-supplied encryption keys (raw, legacy).
- **CombinePerKey** — Beam transform to aggregate per key.

## D–F
- **Data Catalog** — metadata service: tag templates, entries.
- **Dataplex** — unified data governance, quality, and lineage.
- **Dead-letter topic (DLQ)** — where messages go after max delivery attempts.
- **DLP** — Data Loss Prevention API: inspect + de-identify PII.
- **DAG** — Directed Acyclic Graph (Airflow workflow definition).
- **Eventarc** — event-driven routing (GCS/Pub/Sub → services).
- **Exactly-once delivery** — Pub/Sub subscription-level dedup.
- **External table** — BigQuery table reading from files in GCS.
- **FlexRS** — flexible slot pricing for batch Dataflow.
- **Flex Template** — containerized Dataflow template, any language.

## G–L
- **IAM condition** — CEL expression limiting when a binding applies.
- **Ingestion-time partitioning** — partition by `_PARTITIONTIME`.
- **LookML** — Looker modeling language (Views, Explores, Models).
- **Lifecycle rule** — auto class-change/delete on GCS objects.

## M–O
- **Materialized view** — pre-computed, auto-refreshed aggregates.
- **Model Registry** (Vertex AI) — versioned model storage.
- **On-demand pricing** — pay per byte scanned.
- **Ordering keys** — per-key message ordering in Pub/Sub.
- **ParDo** — Beam element-wise transform (DoFn).

## P–S
- **Policy tag** — column-level access control in BigQuery.
- **Partition pruning** — skipping whole partitions via filters.
- **Preemptible/spot VM** — cheap, short-lived compute for fault-tolerant jobs.
- **Pull subscription** — subscriber polls Pub/Sub.
- **Push subscription** — Pub/Sub POSTs to an HTTP endpoint.
- **Schema registry** — validates Pub/Sub message structure (Avro/Protobuf).
- **Seek/Snapshot** — rewind/replay a Pub/Sub subscription.
- **Side input** — broadcast reference data into a Beam transform.
- **Slots** — BigQuery compute units; flat-rate buys a baseline.

## T–Z
- **Templates (Dataflow)** — classic vs flex prebuilt pipelines.
- **Transfer Appliance** — physical offline data migration.
- **Transfer Service** — network data migration/sync.
- **Trigger** — Beam condition controlling when a window emits.
- **Vertex AI** — unified ML platform (training, endpoints, batch, monitoring).
- **VPC-SC** — security perimeter to prevent data exfiltration.
- **Watermark** — Dataflow's estimate of "all data up to time T arrived".
- **Workflow Templates (Dataproc)** — managed multi-job cluster runs.
- **Workflows** — serverless YAML orchestration service.
