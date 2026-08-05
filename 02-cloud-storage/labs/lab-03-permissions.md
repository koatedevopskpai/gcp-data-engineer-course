# Lab 02.3 — Bucket Permissions: Uniform vs Fine-Grained

## Objectives
- Enable uniform bucket-level access (recommended).
- Grant IAM bindings to a service account and (demo only) to a user.
- Inspect bucket IAM.

## Steps

```powershell
$PROJECT_ID = "gcp-data-engineering-course"
$BUCKET = "gs://cymbal-raw-$PROJECT_ID"

# 1. Enable uniform bucket-level access
gsutil uniformbucketlevelaccess set on $BUCKET

# 2. Grant object viewer to the course service account
gsutil iam ch serviceAccount:data-engineer-sa@$PROJECT_ID.iam.gserviceaccount.com:objectViewer $BUCKET

# 3. (Demo) grant a project-wide role instead — preferred for groups
gcloud projects add-iam-policy-binding $PROJECT_ID `
  --member="group:data-team@example.com" --role="roles/storage.objectViewer"

# 4. Remove public access (anti-pattern) if present
gsutil iam ch -d allUsers:objectViewer $BUCKET

# 5. Inspect
gsutil iam get $BUCKET
```

## Concept: Uniform vs fine-grained
- **Uniform bucket-level access**: all access via IAM on the bucket; ACLs are
  disabled. Simpler, recommended, works with VPC-SC.
- **Fine-grained**: per-object ACLs. Legacy; only needed for per-object sharing.

## Exam notes
- `storage.objectViewer` = read objects; `storage.objectAdmin` = full object control.
- Bucket-level IAM + uniform access is the default exam answer for "how to control access to objects".
