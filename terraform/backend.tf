terraform {
  backend "azurerm" {
    resource_group_name  = "<The resource group containing your state file"
    storage_account_name = "<The name of the storage account containing your state file"
    container_name       = "tfstate"
    key                  = "<your tfstate file>"
  }
}
