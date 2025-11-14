# CI/CD Pipelines – Terraform Landing Zone

This document explains the CI/CD automation used for the landing zone, originally implemented in Azure DevOps using YAML pipelines.

---

## Overview

Three pipelines orchestrate Terraform actions:

1. **PR Validation Pipeline** → `pr-validate.yml`
2. **Plan/Apply Pipeline (main branch)** → `plan-apply.yml`
3. **Destroy Pipeline (manual)** → `destroy.yml`

The pipelines enforce:
- Formatting standards
- Terraform validation
- Zero-drift planning
- Manual approvals for production applies
- Remote-backend use

---

## 1. Pull Request Validation Pipeline

Runs on all PRs targeting `main`.

### Validations Performed

- `terraform fmt -check` (enforces formatting)
- `terraform init`
- `terraform validate`
- `terraform plan` (no apply)
- Export SPN → ARM_* variables
- Guard rails to prevent missing environment variables

### Why it matters:
- Prevents broken IaC from merging
- Ensures consistent style
- Shows reviewers the exact plan output

---

## 2. Plan-Apply Pipeline (Main Branch)

Triggered on push → `main`.

### Steps

1. Install Terraform on agent
2. Initialize backend (remote state)
3. Generate plan
4. Wait for manual approval
5. Apply changes to Azure

### Controls:
- Requires approval before apply
- Uses remote backend for state locking
- Uses service principal with minimal permissions

---

## 3. Destroy Pipeline

Manual pipeline to tear down resources.

Used for:
- Cleanup during development
- Rebuilding the environment from scratch
- Demos / testing

Requires:
- Manual run
- Explicit environment approval (optional)

---

## Security Considerations

- Secrets stored in variable groups in ADO
- No secrets stored in repository
- SPN exported to ARM_* variables securely
- Pipelines restricted by branch protection

---

## Future Enhancement (GitHub Actions)

This repo can be upgraded to GitHub Actions with workflows for:

- PR validation  
- Plan / apply with approvals  
- OIDC-based authentication  
- Drift detection (nightly plan)  

*(Ask me if you want the GH Actions YAML too.)*

