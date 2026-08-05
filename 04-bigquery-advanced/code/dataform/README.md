# Dataform project — Cymbal Retail

Minimal Dataform project used in Lab 04.6.

```
definitions/
├── staging/stg_taxi.sqlx
├── marts/fct_daily_sales.sqlx
└── assertions/stg_taxi_assertions.sqlx
dataform.json
package.json
```

To run:
```bash
npm i -g @dataform/cli
dataform install
dataform compile
dataform run
```

> `dataform.json` normally contains your BigQuery `defaultSchema`, `warehouse`,
> and `defaultLocation`; keep secrets out of the repo (use `dataform config` + env vars).
