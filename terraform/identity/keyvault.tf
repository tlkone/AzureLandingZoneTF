# Pull current tenant + subscription details
data "azurerm_client_config" "current" {}

# Create the Key Vault
resource "azurerm_key_vault" "kv" {
  name                = var.kv_name
  location            = var.location
  resource_group_name = azurerm_resource_group.identity.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"

  soft_delete_retention_days    = 90
  purge_protection_enabled      = true
  public_network_access_enabled = true

  tags = {
    environment = "landingzone"
    layer       = "identity"
  }
}

# Add an access policy for yourself (for testing)
resource "azurerm_key_vault_access_policy" "self" {
  key_vault_id = azurerm_key_vault.kv.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id

  key_permissions = [
    "Get", "List", "Create", "Delete", "Recover", "Backup", "Restore"
  ]

  secret_permissions = [
    "Get", "List", "Set", "Delete", "Recover", "Backup", "Restore"
  ]

  certificate_permissions = [
    "Get", "List", "Create", "Delete", "Recover"
  ]
}
