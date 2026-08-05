# Terraform: course infrastructure

Deploys the shared course resources. **Always `terraform destroy` after a lab
block** to protect the $300 free credits.

```bash
terraform init
terraform plan -var="project_id=gcp-data-engineering-course"
terraform apply -var="project_id=gcp-data-engineering-course"
# ... labs ...
terraform destroy -var="project_id=gcp-data-engineering-course"
```

Windows PowerShell:
```powershell
terraform apply -var="project_id=gcp-data-engineering-course"
```

> Resources NOT created here on purpose (cost/size): Composer environment,
> Dataproc cluster, Dataflow jobs, Vertex AI endpoints — those are created and
> deleted per-lab.
