# Lab 03.6 — Slots, Pricing & Cost Control

## Objectives
- Explain on-demand vs flat-rate (reservation) pricing.
- Inspect slot usage and bytes billed.
- Keep course queries inside the 1 TB/month free tier.

## 1. Pricing model
- **On-demand**: pay per byte scanned (1 TB/month free tier). Default.
- **Flat-rate (reservations)**: buy a baseline of slots; predictable cost; best
  for heavy, steady workloads.

## 2. See how much you scan (cost = bytes billed)
```sql
SELECT
  job_id,
  user_email,
  total_bytes_billed / POWER(1024,3) AS gb_billed,
  total_slot_ms,
  query
FROM `region-us-central1`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE state = 'DONE'
ORDER BY total_bytes_billed DESC
LIMIT 10;
```

## 3. Create a small reservation (only if budget allows)
```bash
bq mk --project_id=<PROJECT_ID> --location=us-central1 --capacity_commitment \
  --plan=FLEX --slots=100 --commitment_end_time=+60
bq mk --project_id=<PROJECT_ID> --location=us-central1 --reservation=sales_res \
  --slots=100 --ignore_idle_slots=true
bq mk --project_id=<PROJECT_ID> --location=us-central1 --assignment=cymbal_warehouse \
  --reservation_id=projects/<PROJECT_ID>/locations/us-central1/reservations/sales_res \
  --job_type=QUERY
```

## Cost-saving tips (also good exam answers)
- Filter/partition before aggregating; select only needed columns.
- Use **materialized views** for repeated aggregations.
- Query **Parquet over CSV** — scans compressed, smaller files.
- Use **wildcard tables + `_TABLE_SUFFIX`** to restrict partitions.
- Set **table expiration** on scratch tables.

## Exam notes
- On-demand is the default exam assumption unless a question mentions
  predictable/steady workload or "flat rate".
- `total_slot_ms` and `bytes billed` appear in exam performance scenarios.
