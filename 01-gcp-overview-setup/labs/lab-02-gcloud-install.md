# Lab 01.2 — Install and Configure gcloud CLI

## Objectives
- Install the Google Cloud SDK.
- Initialize gcloud and log in.
- Verify the active project.

## Steps (Windows PowerShell)

### 1. Install
```powershell
choco install googlecloudsdk
# or run GoogleCloudSDKInstaller.exe from https://cloud.google.com/sdk/docs/install
```

macOS / Linux / WSL:
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

### 2. Initialize
```powershell
gcloud init
# Follow prompts: authenticate, then select/create the project gcp-data-engineering-course
```

### 3. Log in (user + application default credentials)
```powershell
gcloud auth login
gcloud auth application-default login
gcloud config set project gcp-data-engineering-course
```

### 4. Verify
```powershell
gcloud config list
gcloud version
gcloud auth list
```

## Key concepts
- `gcloud config set project` — sets default project for all commands.
- `gcloud auth application-default login` — gives local SDK libraries (Python,
  Java) the credentials they need.
