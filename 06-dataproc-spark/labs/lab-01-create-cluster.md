# Lab 06.1 — Create a Dataproc Cluster (cost-aware)

## Objectives
- Create a cluster with preemptible workers.
- Add auto-scaling and `--max-idle` auto-deletion for cost control.
- Delete the cluster when the lab is done.

## Steps

```powershell
# Standard cluster with preemptible workers + auto-delete after 20 min idle
gcloud dataproc clusters create taxi-cluster `
  --region=us-central1 `
  --master-machine-type=n1-standard-2 `
  --worker-machine-type=n1-standard-2 `
  --num-workers=2 `
  --num-preemptible-workers=2 `
  --max-idle=20m `
  --image-version=2.0-debian10 `
  --enable-component-gateway

# Verify
gcloud dataproc clusters describe taxi-cluster --region=us-central1
gcloud dataproc clusters list --region=us-central1
```

## Autoscaling policy (optional)
```powershell
# policy.yaml
# workerConfig: {minInstances: 2, maxInstances: 6}
# basicAlgorithm: {yarnConfig: {scaleUpFactor: 0.5, scaleDownFactor: 0.5}}
gcloud dataproc autoscaling-policies import taxi-autoscale-policy `
  --source=policy.yaml --region=us-central1
```

## Cleanup (ALWAYS)
```powershell
gcloud dataproc clusters delete taxi-cluster --region=us-central1
```

## Exam notes
- **Preemptible/spot workers** cut compute cost ~60–80%; best for stateless,
  failure-tolerant jobs (Spark is ideal).
- **Cluster types**: standard vs flex — flex clusters auto-scale during batch
  jobs and go to zero afterward (newer, cost-effective for spiky workloads).
- Component gateway exposes Jupyter/Hive/Spark UIs.
