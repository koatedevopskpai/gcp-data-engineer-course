# Lab 09.2 — Multi-Page Report

## Objectives
- Build a 3-page executive report from the taxi data source.

## Page 1 — Executive Dashboard
- KPIs: Total Revenue (`SUM(total_amount)`), Trip Count (`COUNT(*)`), Avg Fare.
- Time series: revenue by day.

## Page 2 — Vendor Analysis
- Bar chart: revenue by `vendor_id`.
- Pie chart: share by vendor.
- Table: vendor × payment_type totals.

## Page 3 — Geographic Analysis
- Geo map: trips by `pickup_location`.
- Table: top pickup/dropoff locations.

## Steps
1. In the report, click **Page → Duplicate** to create pages 2 and 3.
2. Add charts from the toolbar; bind to the taxi data source.
