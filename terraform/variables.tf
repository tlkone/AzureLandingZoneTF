variable "location" {
  type    = string
  default = "eastus"
}
variable "name_prefix" {
  type    = string
  default = "lz"
} # short, lowercase
variable "suffix" {
  type    = string
  default = "tf"
}

variable "management_group_id" {
  description = "The ID of the Management Group to apply policies to."
  type        = string
  # You can optionally set a default value here if it's not always provided 
  # via the command line, environment variables, or tfvars file.
  # default     = "LandingZones" 
}
