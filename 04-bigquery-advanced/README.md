# Module 04 — BigQuery Advanced

Analytics engineering on BigQuery: nested/repeated data, window functions,
authorized views, UDFs, BI Engine + materialized views, and Dataform.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-nested-repeated.md` | `STRUCT`/`ARRAY` + `UNNEST` patterns |
| `labs/lab-02-window-cte.md` | Window functions, CTEs, `QUALIFY` |
| `labs/lab-03-authorized-view.md` | Authorized views sharing data without grants |
| `labs/lab-04-udf.md` | Persistent SQL and JavaScript UDFs |
| `labs/lab-05-bi-engine-materialized.md` | BI Engine + materialized views |
| `labs/lab-06-dataform.md` | SQL-first pipeline with Dataform |
| `code/sql/module04.sql` | All module queries in one runnable file |
| `code/dataform/` | Example Dataform project (incl. `README.md`) |
| `exercises/exercises.md` | Self-check questions |

## Exam notes

- `UNNEST` flattens arrays; use `CROSS JOIN UNNEST(...)` for nested/repeated.
- **Authorized views** let a view owner expose data without sharing the
  underlying table — safer than sharing the table directly.
- **Materialized views** trade storage for big query speedups and can be
  auto-refreshed; BI Engine accelerates dashboards at low cost.
- Dataform = SQL-first (dataform.json, `.sqlx`) vs dbt = Jinja SQL — same
  transformation concept, different tooling.
