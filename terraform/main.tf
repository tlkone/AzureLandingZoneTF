module "management" {
  source   = "./management"
  location = var.location
  rg_name  = local.rg_mgmt
  law_name = local.law_name
}

module "connectivity" {
  source     = "./connectivity"
  location   = var.location
  rg_hub     = local.rg_hub
  rg_spoke   = local.rg_spoke
  vnet_hub   = local.vnet_hub
  vnet_spoke = local.vnet_spk
}

module "identity" {
  source   = "./identity"
  location = var.location
  rg_name  = local.rg_id
  kv_name  = local.kv_name
}

module "policy" {
  source   = "./policy"
  location = var.location
  management_group_id = "LandingZones" # or your actual MG ID
  #management_group_id = local.management_group_id
  log_analytics_id    = module.management.law_id
}



