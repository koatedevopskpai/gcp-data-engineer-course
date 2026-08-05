# Lab 10.1 — Custom IAM Role + IAM Conditions

## Objectives
- Create a custom IAM role with a permission list.
- Assign it with an IAM condition.

## 1. Create the custom role
```powershell
gcloud iam roles create data_engineer_course `
  --project=gcp-data-engineering-course `
  --title="Data Engineer Course" `
  --description="Read BigQuery and manage Storage objects" `
  --permissions=bigquery.jobs.create,bigquery.jobs.get,bigquery.tables.get,bigquery.tables.getData,bigquery.tables.list,storage.objects.get,storage.objects.list,storage.objects.create `
  --stage=GA
```

Using the JSON file (`code/custom-role.json`):
```powershell
gcloud iam roles create data_engineer_course --project=gcp-data-engineering-course --file=code\custom-role.json
```

## 2. Assign with an IAM condition
```powershell
gcloud projects add-iam-policy-binding gcp-data-engineering-course `
  --member="user:alice@example.com" `
  --role="projects/gcp-data-engineering-course/roles/data_engineer_course" `
  --condition="expression=resource.name.startsWith('projects/_/buckets/cymbal-'),title=Bucket-prefix,description=Only cymbal buckets"
```

## Exam notes
- **Primitive** (Owner/Editor/Viewer) → broad, avoid.
- **Predefined** (e.g., `roles/bigquery.dataViewer`) → Google-managed granular.
- **Custom** → your own role with explicit permissions.
- **IAM conditions** attach CEL expressions (resource, tag, date) to bindings.

## Verify effective permissions
```powershell
gcloud projects get-iam-policy gcp-data-engineering-course --flatten="bindings[].members" --format="table(bindings.role,bindings.members)"
```
