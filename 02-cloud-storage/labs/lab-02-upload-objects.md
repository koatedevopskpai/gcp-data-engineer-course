# Lab 02.2 — Upload Objects via Console and gsutil

## Objectives
- Upload via the console and via gsutil.
- Copy public sample data into the raw bucket.
- Understand `cp`, `mv`, `rsync`, and parallel composite uploads.

## Steps

```powershell
$PROJECT_ID = "gcp-data-engineering-course"
$BUCKET = "gs://cymbal-raw-$PROJECT_ID"

# Create a sample file
"vendor_id,fare_amount,trip_distance,pickup_datetime,payment_type" | Out-File -Encoding utf8 taxi_trips_sample.csv
"VTS,12.50,3.4,2024-01-01T10:00:00Z,CRD" | Out-File -Encoding utf8 -Append taxi_trips_sample.csv

# Upload single file
gsutil cp taxi_trips_sample.csv $BUCKET/

# Upload directory recursively
gsutil cp -r .\data\ $BUCKET/data/

# Copy public sample data (used by Modules 3+)
gsutil cp -r gs://cloud-samples-data/bigquery/sample-transactions/ $BUCKET/sample-transactions/

# Parallel composite upload (large files, gzip for text)
gsutil -o GSUtil:parallel_composite_upload_threshold=150M cp large_file.csv $BUCKET/

# Incremental sync (mirror a folder)
gsutil rsync -r .\data\ $BUCKET/data/

# List objects
gsutil ls -l $BUCKET/
```

## Exam notes
- `gsutil cp` always stores with metadata; to force re-upload use `-r`.
- **Parallel composite uploads** speed up large files but are not recommended
  for very small files (overhead).
- Set `Content-Encoding: gzip` for compressible text to cut egress and cost.
