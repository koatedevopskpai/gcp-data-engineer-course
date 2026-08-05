# Environment Setup

Cross-platform guide. Commands are shown for **Windows PowerShell** first; the
bash variant is the same command without the PowerShell-specific bits.

## 1. Install Google Cloud SDK

**Windows**
```powershell
# Option A: Chocolatey
choco install googlecloudsdk

# Option B: silent installer (from https://cloud.google.com/sdk/docs/install)
# Run GoogleCloudSDKInstaller.exe, then in a NEW terminal:
gcloud version
```

**macOS**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud version
```

**Linux / WSL**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud version
```

## 2. Install Python

**Windows**
```powershell
winget install Python.Python.3.12
# or use the installer from python.org (check "Add python.exe to PATH")
```

**macOS/Linux**
```bash
brew install python@3.12   # macOS
sudo apt install python3.12 python3.12-venv   # Debian/Ubuntu
```

Verify:
```powershell
python --version
```

## 3. Authenticate

```powershell
gcloud init                                   # log in and select/create a project
gcloud auth login                             # browser-based user login
gcloud auth application-default login         # ADC for local SDK libraries
gcloud config set project YOUR_PROJECT_ID
gcloud config list
```

## 4. Python virtual environment + dependencies

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1                  # PowerShell
# macOS/Linux: source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Service-account key (for server-side jobs)

```powershell
gcloud iam service-accounts create data-engineer-sa --display-name="Data Engineer SA"
gcloud iam service-accounts keys create sa-key.json `
  --iam-account="data-engineer-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com"
$env:GOOGLE_APPLICATION_CREDENTIALS = "$PWD\sa-key.json"
```

## 6. Final verification

```powershell
gcloud config get-value project
gsutil ls
bq ls
python -c "from google.cloud import bigquery; print('OK', bigquery.Client().project)"
```

## Troubleshooting

- **"Authentication failed"**: re-run `gcloud auth login` and
  `gcloud auth application-default login`.
- **`bq`/`gsutil` not found on Windows**: restart the terminal so PATH refreshes.
- **pip installs fail on Windows**: install
  [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
  (needed by `apache-beam`/`pandas` wheels) and retry.
