terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.90.0"
    }
  }
}

provider "azurerm" {
  features {}
  # Add your specific Subscription ID here:
  subscription_id = "<yoursubscriptionID>"
  # You might also need the tenant ID if you have access to multiple tenants:
  # tenant_id       = "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
}
