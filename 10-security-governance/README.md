# Module 10 — Security & Governance

Protect data: custom IAM roles, policy tags + Data Catalog, VPC Service
Controls, DLP redaction, and audit logging.

## Contents

| File | Purpose |
|---|---|
| `labs/lab-01-custom-iam.md` | Create + bind a custom IAM role |
| `labs/lab-02-data-catalog-policy-tags.md` | Policy tags, taxonomy, tag policies (Data Catalog) |
| `labs/lab-03-vpc-sc.md` | VPC Service Controls perimeter |
| `labs/lab-04-dlp.md` | Cloud DLP: inspect + deidentify/redact |
| `labs/lab-05-audit-logs.md` | Cloud Audit Logs, data access logs |
| `code/custom-role.json` | Custom IAM role definition |
| `code/taxonomy.json` | Policy-tag taxonomy definition |
| `code/policy-tag-policy.json` | Policy-tag `set-iam-policy` bindings |
| `code/tag.json` | Tag (catalog entry) reference |
| `code/dlp_redact.py` | DLP redaction script (verified) |
| `exercises/exercises.md` | Self-check questions |

## Verified gotchas (2026)

- **Data Catalog tag templates and tags are DEPRECATED** — write operations
  return `INVALID_ARGUMENT` ("not allowed ... due to Data Catalog
  deprecation"). **Policy tags (taxonomy import) still work** and are the
  focus of Lab 02; Dataplex aspect-types are the modern successor.
- `set-iam-policy` takes the policy file **positionally**
  (`gcloud ... set-iam-policy <resource> policy.json`); `--policy-file`
  is rejected.
- DLP's SSN detector deliberately **ignores dummy values** like
  `123-45-6789`; use a realistic-but-unissued SSN (e.g. `078-05-1120`) so the
  redaction demo actually redacts. `crypto_deterministic_config` requires a
  real `wrapped_key` — the lab uses a verified plain deidentify transform.

## Exam notes

- **DLP** inspects (info types: `US_SOCIAL_SECURITY_NUMBER`, `EMAIL_ADDRESS`,
  `PERSON_NAME`, …) and deidentifies (redact, mask, tokenize,
  format-preserving, crypto-based).
- **Policy tags** attach to BigQuery columns and are enforced via
  `roles/datacatalog.categoryFineGrainedReader`.
- **VPC-SC** defines service perimeters (allow/deny lists) — an
  organization-level security control.
- Audit logs: admin activity (always on), data access (opt-in), policy
  denied (always on).
