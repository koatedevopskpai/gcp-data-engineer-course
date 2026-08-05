# Lab 10.2 — Data Catalog, Tag Templates & Policy Tags

## Objectives
- Create a Data Catalog tag template.
- Create a policy tag taxonomy for **column-level security**.
- Attach a policy tag to `taxi_trips.payment_type`.

## 1. Data Catalog tag template
```powershell
# Enable the API first (idempotent — safe to run even if already enabled)
gcloud services enable datacatalog.googleapis.com

gcloud data-catalog tag-templates create pii_template `
  --location=us-central1 `
  --display-name="PII Template" `
  --field=id=pii_type,display-name="PII Type",type=string,required=TRUE `
  --field=id=classification,display-name="Classification",type=string,required=TRUE
```

Attach a tag to a table entry:
```powershell
gcloud data-catalog tags create `
  --location=us-central1 `
  --tag-template=pii_template `
  --tag-file=code\tag.json `
  --entry=projects/gcp-data-engineering-course/locations/us-central1/entryGroups/@bigquery/entries/cymbal_warehouse.taxi_trips
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

# 2. Confirm it exists; the output shows the taxonomy's resource name
gcloud data-catalog taxonomies list --location=us-central1
# e.g. projects/<PROJECT_NUMBER>/locations/us-central1/taxonomies/<TAXONOMY_ID>

# 3. List the policy tags inside it (copy the PII / Payment policy tag name)
gcloud data-catalog taxonomies policy-tags list --location=us-central1 --taxonomy=<TAXONOMY_NAME>

# 4. Restrict who can access columns tagged with the policy tag
#    (policy-file grants roles/datacatalog.policyTagViewer or roles/datacatalog.categoryFineGrainedReader)
gcloud data-catalog taxonomies policy-tags set-iam-policy <POLICY_TAG_NAME> `
  --location=us-central1 --taxonomy=<TAXONOMY_NAME> `
  --policy-file=code\policy-tag-policy.json
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
