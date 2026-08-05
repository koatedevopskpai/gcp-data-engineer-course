# Cymbal Retail — Looker Studio Dashboard Guide

## Data sources
Connect Looker Studio to the dbt **marts** dataset (Gold):

| Table | Purpose |
|---|---|
| `marts.fct_daily_sales` | revenue, purchases, views by date + product |
| `cymbal_warehouse.clickstream_raw` | real-time KPIs (raw) |
| `cymbal_warehouse.product_stats_streaming` | real-time product counters |

## Page 1 — Executive Overview
- KPI cards: Total Revenue (24h), Purchases (24h), Conversion Rate.
- Time series: revenue by day (from `fct_daily_sales`).
- Cross-filter on date.

## Page 2 — Product Performance
- Bar chart: top products by revenue (from `fct_daily_sales`).
- Donut: revenue share by product.
- Table: views, add-to-carts, purchases, revenue per product.

## Page 3 — Real-Time Monitor
- Scorecards from `product_stats_streaming` (counts per minute).
- Trend chart: counts over time.

## Metrics / calculated fields
- `Conversion rate = purchases / views`
- `Avg order value = revenue / purchases`

## Acceleration
- Enable **BigQuery BI Engine** (Module 04) on the Gold dataset for snappier
  dashboard queries.

## Sharing
- **Share → Anyone with the link (viewer)** and enable **Schedule email delivery**
  for the executive deck.
