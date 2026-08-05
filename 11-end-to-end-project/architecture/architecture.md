# Cymbal Retail Analytics Platform — Architecture

```
                             ┌──────────────────────────────┐
                             │      Clickstream Simulator    │
                             │       (code/simulator.py)     │
                             └──────────────┬───────────────┘
                                            │ publish (JSON)
                                            ▼
                             ┌──────────────────────────────┐
                             │  Pub/Sub topic               │
                             │  cymbal-clickstream          │
                             └──────────────┬───────────────┘
                                            │ pull subscription
                                            ▼
                             ┌──────────────────────────────┐
                             │  Dataflow (Apache Beam)      │
                             │  code/streaming_pipeline.py  │
                             │  - parse + enrich            │
                             │  - fixed windows + triggers  │
                             └──────────────┬───────────────┘
                                            │
                    ┌───────────────────────┼───────────────────────┐
                    ▼                       ▼                       ▼
        ┌───────────────────┐   ┌───────────────────┐   ┌───────────────────────┐
        │ BigQuery Bronze   │   │ BigQuery Gold     │   │ Cloud Storage         │
        │ clickstream_raw   │   │ product_stats_    │   │ staging/temp + archive│
        │ (raw events)      │   │ streaming (agg)   │   │ (offload, audit)      │
        └─────────┬─────────┘   └─────────┬─────────┘   └───────────────────────┘
                  │                       │
                  └───────────┬───────────┘
                              ▼
                  ┌──────────────────────┐
                  │ dbt (transform)      │
                  │ stg_events →         │
                  │ fct_daily_sales      │
                  └─────────┬────────────┘
                            ▼
                  ┌──────────────────────┐
                  │ Looker Studio        │
                  │ executive dashboard  │
                  │ (BI Engine accel.)   │
                  └──────────────────────┘

     Cloud Composer (code/dags/end_to_end_dag.py), hourly:
     validate → run dbt/backfill → alert on failure
```

## Data flow (medallion)
- **Bronze** — `clickstream_raw`: every event as received.
- **Silver** — dbt `stg_events`: cleaned, typed, deduped.
- **Gold** — dbt `fct_daily_sales`: daily product/session aggregations for the dashboard.

## Cost posture
- Stop the streaming Dataflow job when not demoing.
- Keep the simulator modest (random 0.1–1.0 s sleep).
- Delete Composer env after the capstone demonstration.
