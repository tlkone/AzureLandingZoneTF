locals {
  rg_mgmt  = "rg-mgmt-logging-${var.suffix}"
  rg_hub   = "rg-hub-net-${var.suffix}"
  rg_spoke = "rg-spoke-app1-${var.suffix}"
  rg_id    = "rg-identity-core-${var.suffix}"

  law_name = "law-core-${var.suffix}"
  kv_name  = "kv-core-${var.suffix}${random_string.kv_suffix.result}"

  vnet_hub = "vnet-hub-${var.suffix}"
  vnet_spk = "vnet-spoke-app1-${var.suffix}"
}
resource "random_string" "kv_suffix" {
  length  = 3
  upper   = false
  special = false
}
