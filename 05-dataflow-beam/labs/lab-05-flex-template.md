# Lab 05.5 — Flex Template (parameterized pipeline)

## Objectives
- Turn a parameterized pipeline into a Flex Template.
- Stage the template on GCS.
- Run the template from the console/CLI without code.

## 1. Parameterized pipeline (`code/flex_template_pipeline.py`)
```python
def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    known, pipeline_args = parser.parse_known_args(argv)
    with beam.Pipeline(options=PipelineOptions(pipeline_args)) as p:
        (p
         | "Read" >> beam.io.ReadFromText(known.input)
         | "Split" >> beam.FlatMap(lambda x: x.split())
         | "Count" >> beam.combiners.Count.PerElement()
         | "Write" >> beam.io.WriteToText(known.output))
```

## 2. Build the image + template (Docker + gcloud)
```powershell
# build container image
gcloud builds submit --tag gcr.io/gcp-data-engineering-course/wordcount:latest .

# stage the Flex Template on GCS
gcloud dataflow flex-template build `
  gs://cymbal-processed-gcp-data-engineering-course/templates/wordcount.json `
  --image-gcr-path="gcr.io/gcp-data-engineering-course/wordcount:latest" `
  --sdk-language="PYTHON" `
  --metadata-file=metadata.json
```

## 3. Run the template
```powershell
gcloud dataflow flex-template run wordcount-template `
  --region=us-central1 `
  --template-file-gcs-location=gs://cymbal-processed-gcp-data-engineering-course/templates/wordcount.json `
  --parameters="input=gs://dataflow-samples/shakespeare/kinglear.txt,output=gs://cymbal-processed-gcp-data-engineering-course/wordcount/out"
```

## Exam notes
- **Classic templates**: single-file, Python/Java only, built with
  `--template_location`.
- **Flex templates**: Docker image, any language, full dependency control —
  recommended for production.
- Templates let **non-technical users** launch pipelines from the console —
  a common exam scenario (answer: Flex template).
