# Getting Started – Deploying the Landing Zone

This guide explains how to deploy the Azure landing zone from scratch using Terraform.

---

## Prerequisites

### 1. Azure Requirements
- Azure subscription
- Permissions:
  - Management Group Contributor
  - Owner / Contributor on subscription
  - User Access Administrator (optional)

### 2. Tools Installed
- Terraform ≥ 1.5
- Azure CLI
- Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/tlkone/AzureLandingZoneTF.git
cd AzureLandingZoneTF/terraform


---

## 2. Authenticate to Azure

az login
az account set --subscription "<your-subscription-id>"

(Optional) Use a Service Principal for automation:
az ad sp create-for-rbac --name "tf-sp" --role Contributor --scopes /subscriptions/<sub-id>

---

## 3. Configure Backend
Create backend.tfvars:

resource_group_name  = "tfstate-rg"
storage_account_name = "tfstatestorageXXXX"
container_name       = "tfstate"
key                  = "landingzone/dev.tfstate"

---

## 4. Configure Variables
Create terraform.tfvars:

location         = "eastus"
tenant_id        = "<tenant-guid>"
subscription_id  = "<sub-guid>"
mg_prefix        = "platform"
project_name     = "landingzone"

---

## 5. Initialize Terraform

terraform init -backend-config=backend.tfvars

---

## 6. Review the Plan

terraform plan -var-file=terraform.tfvars

---

## 7. Deploy

terraform apply -var-file=terraform.tfvars

---

## 8. Verify Deployment

Check:
- Management Groups created
- Hub/spoke VNets
- Firewall & Bastion
- Log Analytics & Automation
- Policy compliance

---

## 9. Destroy Environment (optional)

terraform destroy -var-file=terraform.tfvars







