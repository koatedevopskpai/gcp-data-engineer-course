# Exam Tips & Strategy

## Know the exam
- 2 hours, ~50 questions. Budget ~2.2 min/question.
- May include **case studies** (read twice, underline constraints).
- Passing score is not published; historically ~70%. Aim for 80%+ on mocks.

## Question strategy
1. **Eliminate absurd answers first** (wrong service, wrong pricing model).
2. Look for "must" words: **fully managed, serverless, low cost, without code,
   no rewrite, sub-second** — they point at a specific service.
3. When two answers look similar, the more **fully managed / simpler / cheaper**
   one is usually the "Google way" answer.
4. Don't change an answer without strong reason. Flag and return.
5. Leave nothing blank — no penalty for guessing.

## Domain-by-domain tips
- **Design (20–25%):** storage class selection, Bigtable vs BigQuery, region/DR,
  transfer tools, cost. Practice the "when to use X vs Y" drills daily.
- **Build & Operationalize (30–35%):** Dataflow vs Dataproc, windows/triggers,
  Composer/Workflows/Scheduler, Pub/Sub semantics, templates. Re-run the streaming
  lab at least twice.
- **ML (15–20%):** BQML functions, Vertex AI pieces, batch vs online, drift. The
  new Module 13 closes this gap.
- **Quality & Governance (15–20%):** policy tags, authorized views, DLP, VPC-SC,
  audit logs, data quality tests.

## Time management
- 25-question mock in ≤60 min; if you exceed, practice faster elimination.
- Reserve the last 10 min for review of flagged questions.

## Common traps
- "Push subscription to Dataflow" — not a thing (Dataflow pulls).
- `GRANT SELECT ... TO "user:"` — not BigQuery syntax (IAM roles instead).
- Confusing **policy tags** (columns) with **authorized views** (subset share).
- Confusing **Transfer Appliance** (offline) with **STS** (network).
- Assuming Flat-rate for one-off queries (use on-demand).
- Confusing **Looker** with **Looker Studio** on the exam.

## Before the exam day
- Run Mock 1 and Mock 2 at least once each, timed, no notes.
- Re-read `cheat-sheets.md` and `glossary.md` the morning of.
- Rebuild one lab from memory (e.g., BQ partitioned table + a Dataflow job).
- Sleep well. Arrive with ID and voucher confirmed.
