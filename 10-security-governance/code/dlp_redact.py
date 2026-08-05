#!/usr/bin/env python
"""Cloud DLP: inspect and de-identify PII in a text sample."""
from google.cloud import dlp_v2

PROJECT_ID = "gcp-data-engineering-course"
TEXT = "Customer: John Doe, Email: john.doe@example.com, SSN: 123-45-6789"


def main() -> None:
    client = dlp_v2.DlpServiceClient()
    parent = f"projects/{PROJECT_ID}"

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
            "item": {"value": TEXT},
        }
    )
    print("Original:", TEXT)
    print("Redacted:", response.item.value)


if __name__ == "__main__":
    main()
