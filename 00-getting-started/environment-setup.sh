#!/usr/bin/env bash
# environment-setup.sh
# One-shot setup for macOS / Linux / WSL. Windows users: use environment-setup.md.
set -euo pipefail

PROJECT_ID="${1:-}"
if [[ -z "$PROJECT_ID" ]]; then
  echo "Usage: $0 YOUR_PROJECT_ID"
  exit 1
fi

echo "==> Installing Google Cloud SDK (if missing)"
command -v gcloud >/dev/null 2>&1 || curl -sSL https://sdk.cloud.google.com | bash

echo "==> Configuring project"
gcloud config set project "$PROJECT_ID"
gcloud auth login --no-launch-browser || gcloud auth login
gcloud auth application-default login

echo "==> Creating virtualenv"
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "==> Creating course service account (least privilege added per-module)"
gcloud iam service-accounts create data-engineer-sa \
  --display-name="Data Engineer Service Account" || true
gcloud iam service-accounts keys create sa-key.json \
  --iam-account="data-engineer-sa@${PROJECT_ID}.iam.gserviceaccount.com"

echo "==> Done. Set GOOGLE_APPLICATION_CREDENTIALS=\$PWD/sa-key.json"
