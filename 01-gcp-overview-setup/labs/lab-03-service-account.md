# Lab 01.3 — Create Service Account and IAM Roles

## Objectives
- Create a service account for the course.
- Grant least-privilege roles (grant more roles in later modules as needed).
- Download a JSON key and use it for authentication.

## Steps

### 1. Create the service account
```powershell
gcloud iam service-accounts create data-engineer-sa --display-name="Data Engineer Service Account"
```

### 2. Grant roles (project-level)
```powershell
$PROJECT_ID = "gcp-data-engineering-course"
$SA = "data-engineer-sa@$PROJECT_ID.iam.gserviceaccount.com"

gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SA" --role="roles/bigquery.jobUser"
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SA" --role="roles/bigquery.dataEditor"
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SA" --role="roles/storage.objectAdmin"
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SA" --role="roles/pubsub.publisher"
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SA" --role="roles/pubsub.subscriber"
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SA" --role="roles/dataflow.admin"
```

> **Least privilege tip:** these roles are enough to start. Dataflow needs
> `roles/dataflow.worker` on the *Dataflow service account* (not the user SA) —
> covered in Module 5.

### 3. Download the key
```powershell
gcloud iam service-accounts keys create sa-key.json --iam-account=$SA
$env:GOOGLE_APPLICATION_CREDENTIALS = "$PWD\sa-key.json"
```

### 4. Activate the service account (optional)
```powershell
gcloud auth activate-service-account --key-file=sa-key.json
```

## Security warning
- Never commit `sa-key.json` to git. Add it to `.gitignore`.
- Prefer workload identity federation / ADC over long-lived keys in production.

## Exam concepts
- **Primitive roles**: Owner/Editor/Viewer (broad, discouraged).
- **Predefined roles**: fine-grained, Google-maintained (`roles/bigquery.*`).
- **Custom roles**: your own `role` with an explicit permission list.
- **Service account** = identity for applications, not people.
