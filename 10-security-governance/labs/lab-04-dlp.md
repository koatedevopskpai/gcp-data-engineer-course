# Lab 10.4 — Cloud DLP: Inspect and De-identify PII

## Objectives
- Scan text/table data for PII (infoTypes).
- Redact/mask findings with de-identification transforms.
- Do it on a BigQuery table via a DLP job.

## 1. Inline de-identify (`code/dlp_redact.py`)
```python
from google.cloud import dlp_v2

project_id = "gcp-data-engineering-course"
client = dlp_v2.DlpServiceClient()
parent = f"projects/{project_id}"

text = "Customer: John Doe, Email: jdoe@example.com, SSN: 078-05-1120"

inspect_config = {
    "info_types": [
        {"name": "EMAIL_ADDRESS"},
        {"name": "PERSON_NAME"},
        {"name": "US_SOCIAL_SECURITY_NUMBER"},
    ],
    "min_likelihood": "LIKELIHOOD_UNSPECIFIED",
}

deidentify_config = {
    "info_type_transformations": {
        "transformations": [
            {"primitive_transformation": {"replace_with_info_type_config": {}}}
        ]
    }
}

response = client.deidentify_content(
    request={
        "parent": parent,
        "inspect_config": inspect_config,
        "deidentify_config": deidentify_config,
        "item": {"value": text},
    }
)
print("Original:", text)
print("Redacted:", response.item.value)
```
> Note: `123-45-6789` (and `111-11-1111`) are deliberately excluded by DLP's
> SSN detector as dummy values — use a realistic number like `078-05-1120` so
> the redaction is visible. Emails whose local part looks like a name
> (`john.doe@example.com`) produce `[PERSON_NAME][EMAIL_ADDRESS][PERSON_NAME]`.

## 2. DLP job over a BigQuery table (console)
1. Console → **Security → DLP → Create job**.
2. Source: BigQuery `cymbal_warehouse.customer_data`.
3. Inspect templates: emails, phones, credit cards, names.
4. Add a **de-identification template**: replace, mask, or tokenize.
5. Destination: a new table `customer_data_redacted`.
6. Run once or **schedule** (daily/weekly).

## Exam notes
- **Inspect** = find PII; **de-identify** = mask/replace/hash/tokenize.
- InfoTypes: EMAIL_ADDRESS, PERSON_NAME, US_SOCIAL_SECURITY_NUMBER,
  CREDIT_CARD_NUMBER, PHONE_NUMBER, LOCATION, DATE_OF_BIRTH ...
- **Replace with info type**, **mask** (`x`-masking), **crypto-deterministic**
  (reversible), **tokenization/pseudonymization** — know which to pick.
- For GDPR/PII-in-BigQuery scenarios, DLP + policy tags are the standard answer.
