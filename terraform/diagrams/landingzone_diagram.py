from diagrams import Diagram, Cluster
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.analytics import LogAnalyticsWorkspaces
from diagrams.azure.security import KeyVaults

with Diagram("Azure Landing Zone (Hub-Spoke)", filename="landingzone-highlevel", outformat="png", show=False, direction="TB"):
    with Cluster("Management Group: LandingZones"):
        with Cluster("rg-mgmt-logging-tf"):
            law = LogAnalyticsWorkspaces("law-core-tf")
        with Cluster("rg-identity-core-tf"):
            kv = KeyVaults("kv-core-tf")
        with Cluster("rg-hub-net-tf"):
            hub_vnet = VirtualNetworks("vnet-hub-tf")
        with Cluster("rg-spoke-app1-tf"):
            spoke_vnet = VirtualNetworks("vnet-spoke-app1-tf")

        hub_vnet - spoke_vnet
        law >> kv
