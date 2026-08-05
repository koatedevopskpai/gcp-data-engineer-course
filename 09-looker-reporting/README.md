# Module 09 — Looker & Looker Studio

BI layer: connect Looker/Looker Studio to BigQuery, build reports, apply
filters, computed fields, and share dashboards.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-connect.md` | Connect Looker Studio to BigQuery |
| `labs/lab-02-report.md` | Build a taxi report from `taxi_trips` |
| `labs/lab-03-filters.md` | Date, dimension, and parameter filters |
| `labs/lab-04-calculated.md` | Calculated fields (e.g. fare per mile) |
| `labs/lab-05-share.md` | Share, embed, and schedule delivery |
| `lookml/model_taxi.model.lkml` | LookML model reference |
| `lookml/view_taxi_trips.view.lkml` | LookML view definition |
| `exercises/exercises.md` | Self-check questions |

## Exam notes

- Looker Studio = free dashboarding over BigQuery; Looker = governed BI with
  a semantic layer (LookML).
- LookML separates **views** (dimensions/measures) from **models** (explores,
  joins, caching) — the source of truth for business definitions.
- Filters push down to BigQuery SQL; caching reduces repeated slot usage.
- **BI Engine** (Module 04 lab 05) accelerates Looker/Looker Studio
  dashboards on the same datasets.
