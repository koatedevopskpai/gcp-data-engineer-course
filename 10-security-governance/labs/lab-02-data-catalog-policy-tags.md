# Lab 10.2 — Data Catalog, Tag Templates & Policy Tags

## Objectives
- Understand Data Catalog's deprecation and its successors.
- Create a policy tag taxonomy for **column-level security**.
- Attach a policy tag to `taxi_trips.payment_type` + restrict who can read it.

> **Deprecation notice (verified live):** Google is deprecating Data Catalog
> *tag templates* and *tags*. `gcloud data-catalog tag-templates create` and
> `gcloud data-catalog tags create` return `INVALID_ARGUMENT: ... not allowed to
> perform write operations due to Data Catalog deprecation`. The successors are
> Dataplex **aspects** (`gcloud dataplex aspect-types`, tags via
> `gcloud dataplex entries`) for metadata/classification.
>
> **Policy tags (fine-grained column access) still work** and are the
> exam-relevant mechanism for BigQuery column-level security — that is the
> focus of this lab.

## 1. Metadata/classification tags (deprecated → use Dataplex)
```powershell
# DEPRECATED - returns INVALID_ARGUMENT on projects with Data Catalog disabled:
gcloud data-catalog tag-templates create pii_template `
  --location=us-central1 `
  --display-name="PII Template" `
  --field=id=pii_type,display-name="PII Type",type=string,required=TRUE

# SUCCESSOR - Dataplex tags/aspects:
gcloud dataplex aspect-types create pii_aspect_type --location=us-central1
```

## 2. Policy tag taxonomy (column-level access)

> **Erratum:** there is **no** `gcloud data-catalog taxonomies create` or
> `gcloud data-catalog taxonomies policy-tags create` command. Taxonomies and
> their policy tags are created in one step by **importing** a serialized
> taxonomy file (JSON/CSV). The file format is the `inlineSource` of the
> ImportTaxonomies API: `{ "taxonomies": [ { "displayName": ..., "policyTags": [...] } ] }`.

```powershell
# 1. Create the taxonomy + policy tags from a file (see code\taxonomy.json)
gcloud data-catalog taxonomies import code\taxonomy.json --location=us-central1
# e.g. projects/<PROJECT>/locations/us-central1/taxonomies/<TAXONOMY_ID>

# 2. List the policy tags inside it (copy the PII / Payment policy tag name)
gcloud data-catalog taxonomies policy-tags list `
  --location=us-central1 --taxonomy=<TAXONOMY_NAME>

# 3. Restrict who can read columns tagged with the policy tag
#    (policy file is a POSITIONAL argument, not --policy-file)
gcloud data-catalog taxonomies policy-tags set-iam-policy <POLICY_TAG_NAME> `
  --location=us-central1 --taxonomy=<TAXONOMY_NAME> `
  code\policy-tag-policy.json
```

## 3. Apply the policy tag to a column (console or bq)
Console: BigQuery → table schema → `payment_type` → **Edit schema → add policy tag**.
Or via `bq` with a schema that includes:
```json
{ "name": "payment_type", "type": "STRING",
  "policyTags": { "names": ["projects/<PROJECT>/locations/us-central1/taxonomies/.../policyTags/..."] } }
```

## Exam notes
- **Policy tags** = column-level security (fine-grained access).
- **Tag templates** = metadata / classification (governance, not security).
- Users without the policy-tag binding cannot read that column even with
  table read access.
