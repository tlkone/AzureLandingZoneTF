terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstatestorage88kt79"
    container_name       = "tfstate"
    key                  = "landingzone/infratk.tfstate"
  }
}
