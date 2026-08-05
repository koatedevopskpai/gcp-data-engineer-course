# Lab 02.4 — CMEK Encryption with Cloud KMS

## Objectives
- Create a Cloud KMS key ring and key.
- Create a bucket encrypted with **CMEK** (customer-managed key).
- Grant the encrypter/decrypter role to the service account.

## Steps (Windows PowerShell)

```powershell
$PROJECT_ID = "gcp-data-engineering-course"
$LOCATION = "us-central1"

# 1. Create key ring + key
gcloud kms keyrings create data-keyring --location $LOCATION
gcloud kms keys create storage-key --location $LOCATION --keyring data-keyring --purpose encryption

# 2. Create a bucket using the CMEK key
gsutil mb -l $LOCATION `
  -k projects/$PROJECT_ID/locations/$LOCATION/keyRings/data-keyring/cryptoKeys/storage-key `
  gs://cymbal-cmek-$PROJECT_ID

# 3. Grant encrypter/decrypter to the course SA (needed to read/write objects)
gcloud kms keys add-iam-policy-binding storage-key `
  --location $LOCATION --keyring data-keyring `
  --member "serviceAccount:data-engineer-sa@$PROJECT_ID.iam.gserviceaccount.com" `
  --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"
```

## Encryption model (exam-critical)
- **Google-managed** (default): GCP owns and rotates keys.
- **CMEK**: you manage the key in Cloud KMS; Google encrypts with it. You can
  disable/delete the key to permanently destroy data.
- **CSEK** (customer-supplied): you supply raw keys directly — deprecated in favor
  of CMEK on most services; Cloud Storage still supports CSEK.
- **CSE** (confidential VMs / CSE on supported services) is a separate model.

## Exam notes
- CMEK allows **key rotation** and **key access control** via KMS IAM.
- Deleting a CMEK key makes data **unrecoverable** — Google cannot decrypt it.
