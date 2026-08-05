# Exam-Style Case Studies

The exam may include multi-paragraph case studies. Use the **answer template**:
(1) restate the requirement, (2) pick the primary fully-managed service,
(3) justify why alternatives fail, (4) mention cost/security if relevant.

---

## Case Study 1 — Global Retailer "Cymbal"

**Scenario:** Cymbal processes 200 TB/day of clickstream + sales. Requirements:
- Real-time dashboards (<1 min latency) for executives.
- Historical analytics in a warehouse.
- Anomaly alerts when sales drop >30% vs 7-day average.
- GDPR: PII must be masked before analytics.
- Budget: prefer serverless/managed; must stay cost-predictable.

**Questions**
1. Choose the ingestion + processing architecture.
2. Where should the warehouse live, and how do you keep dashboards fast?
3. How do you detect sales-drop anomalies in near real time?
4. How do you mask PII before analytics without changing the pipeline's consumers?
5. How do you keep cost predictable?

**Model answer (partial):**
1. **Pub/Sub** (ingestion) → **Dataflow** streaming (windows/triggers, side inputs).
2. **BigQuery** native partitioned/clustered tables + **BI Engine** for dashboards.
3. **Dataflow** windowed aggregation compares current window to the trailing
   7-day average (side input or BigQuery window function), writing anomalies to a
   table; **Cloud Monitoring / Pub/Sub alert** on that table.
4. **Cloud DLP** job (or Dataflow + DLP de-identification) masks PII into a
   separate table; policy tags restrict sensitive columns.
5. On-demand BigQuery + budgets/alerts; scale Dataflow workers with a max cap;
   stop streaming jobs when not needed.

---

## Case Study 2 — Logistics IoT Fleet

**Scenario:** A fleet streams GPS/temperature every 10 seconds from 50,000
vehicles. Needs:
- Sub-second lookup of a vehicle's latest reading.
- Cold-path analytics of historical readings.
- Exactly-once ingest with 5-minute late-arrival tolerance.

**Questions**
1. Best store for the live "latest reading" (low latency, high throughput)?
2. Best streaming processor and windowing config for the 5-minute lateness?
3. How do you achieve exactly-once end to end?

**Model answer:**
1. **Cloud Bigtable** — keyed by vehicle_id, low-latency point reads. BigQuery
   would be too slow for point lookups.
2. **Dataflow**, fixed or session windows with `allowed_lateness=300` (5 min),
   late triggers; write aggregates to BigQuery.
3. Pub/Sub subscription **exactly-once delivery** + BigQuery **Storage Write API
   dedup by primary key**; or idempotent aggregation keys.

---

## Case Study 3 — Legacy Hadoop Migration

**Scenario:** A bank runs 5 PB in on-prem Hadoop (HDFS) with Spark jobs and wants
to move to GCP while keeping costs low and not rewriting everything at once.

**Questions**
1. Which services replace HDFS + Spark with minimal rewrite?
2. How do you migrate the 5 PB?
3. How do you control cost during the transition?

**Model answer:**
1. **Cloud Storage** (HDFS-compatible `gs://`) + **Dataproc** (managed Spark/Hive),
   using the Cloud Storage connector — minimal code change.
2. **Transfer Appliance** for the bulk offline copy (5 PB over WAN is impractical);
   then ongoing incremental sync via **Storage Transfer Service**.
3. **Preemptible workers**, autoscaling, `--max-idle`, delete clusters between
   jobs; budget alerts.

---

## Practice tips
- Read the case study twice. Underline constraints (latency, cost, security,
  "must not rewrite", "fully managed").
- The exam rewards **managed + simple**: when in doubt, BigQuery/Dataflow over
  self-managed clusters.
