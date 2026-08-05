# Getting Started

Everything you need before starting Module 01.

## Contents

| File | Purpose |
|---|---|
| `prerequisites.md` | Account, hardware, and software requirements |
| `environment-setup.md` | Step-by-step local setup for Windows / macOS / Linux |
| `requirements.txt` | Python dependencies for the whole course |
| `environment-setup.sh` | One-shot bash setup (macOS/Linux/WSL) |

## TL;DR

```bash
# 1. Create a GCP account + project (free $300 credits)
# 2. Install Google Cloud SDK + Python 3.10+
# 3. Authenticate
gcloud auth login
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID

# 4. Install Python deps
pip install -r requirements.txt

# 5. Set budget + alerts FIRST (see Module 01 Lab 5)
```

## Cost policy for this course

Every lab in this course is designed to run **inside the $300 free credits**:

1. Create a billing **budget with alerts** before any other lab.
2. **Delete** Composer environments, Dataproc clusters, Dataflow jobs, Vertex AI
   endpoints, and BigQuery reservations when a lab is finished.
3. Use **preemptible workers** on Dataproc.
4. Prefer **on-demand** BigQuery pricing and only query what you need.
5. Streaming jobs are the most expensive — stop them between labs.

Never leave a long-running streaming pipeline or a Composer environment running overnight.
