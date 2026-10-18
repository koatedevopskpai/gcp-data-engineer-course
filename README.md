# Google Cloud Professional Data Engineer — Complete Course Package

Hands-on, exam-aligned course with all code and artifacts. Prepared as the
corrected successor to `gcp-data-professional-exam-prep_Udemy_Course.txt`.

## What changed vs the original draft
See `COURSE-MASTER.md → Errata` for the full list. Highlights:
- New **Module 13: Machine Learning** (BQML + Vertex AI) — closes the 15–20% domain.
- **Fixed** the "push subscription to Dataflow" error (Dataflow pulls) and the
  invalid authorized-view/`GRANT` syntax.
- **50 practice questions with explanations** + 2 mock exams + case studies
  (was 5 questions, no explanations).
- Added **Bigtable, Dataform, Dataplex, external tables, slots/cost, policy tags,
  Windows setup, cost-control labs**.
- Cleaned all broken code fences/artifacts.

## Structure

```
00-getting-started/        setup, prerequisites, requirements.txt
01-gcp-overview-setup/     labs, custom IAM role, budget lab
02-cloud-storage/          lifecycle policy, gsutil commands, CMEK, transfer
03-bigquery-fundamentals/  schema.json, load scripts, external tables, slots
04-bigquery-advanced/      nested/window/UDF/authorized-view SQL, Dataform
05-dataflow-beam/          wordcount, ETL, streaming, side inputs, flex template
06-dataproc-spark/         PySpark, Spark SQL, BigQuery connector, workflow tmpl
07-pubsub-streaming/       publisher/subscriber, DLQ, push CF, schema (CORRECTED)
08-composer-workflow/      DAGs, Workflows YAML, alerting policy
09-looker-reporting/       Looker Studio labs + LookML reference
10-security-governance/    custom role, policy tags, VPC-SC, DLP, audit logs
11-end-to-end-project/     Cymbal Retail: simulator, pipeline, dbt, DAG, dashboard
12-exam-preparation/       study plan, 50 Q&A, 2 mocks, case studies, cheat sheets, glossary
13-machine-learning/       BQML labs + Vertex AI (NEW)
infrastructure/terraform/  IaC for buckets/BQ/Pub/Sub/SA
resources/                 recording guide, course README
COURSE-MASTER.md           corrected master document
```

## Quick start
```bash
git clone https://github.com/koatedevopskpai/gcp-data-engineer-course.git
cd gcp-data-engineer-course
gcloud config set project YOUR_PROJECT_ID
export PROJECT_ID=YOUR_PROJECT_ID          # PowerShell: $env:PROJECT_ID = "YOUR_PROJECT_ID"
python -m venv .venv && source .venv/bin/activate   # PowerShell: .venv\Scripts\Activate.ps1
pip install -r 00-getting-started/requirements.txt
cd infrastructure/terraform
terraform apply -var="project_id=YOUR_PROJECT_ID"
```

> All Python code and DAGs read the project from the `PROJECT_ID` environment
> variable (falling back to `gcp-data-engineering-course`), so every script
> works on any project without edits.

## Cost policy
Always `terraform destroy` / delete Composer, Dataproc, Dataflow, and Vertex
endpoints after labs (see `01-gcp-overview-setup/labs/lab-05-budget-cost-control.md`).

## License
For course/education use. Public datasets remain subject to their own licenses.
