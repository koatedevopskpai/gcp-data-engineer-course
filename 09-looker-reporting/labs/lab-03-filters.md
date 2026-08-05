# Lab 09.3 — Dashboard with Filters

## Objectives
- Add interactive filters and cross-filtering.

## Steps
1. **Add a control → Date range** (binds to `pickup_datetime`).
2. **Add a control → Drop-down list** for `vendor_id`.
3. **Add a control → Slider** for `fare_amount`.
4. Click a chart → **Style → enable Cross-filtering**.
5. Test that charts update together.

## Exam notes
- Looker Studio controls apply report-wide by default; set scope per chart when needed.
- Cross-filtering lets one chart filter others — a common requirement.
