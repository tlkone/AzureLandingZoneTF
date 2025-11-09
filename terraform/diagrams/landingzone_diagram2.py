from diagrams import Diagram, Cluster
from diagrams.azure.compute import VM
from diagrams.azure.network import VirtualNetworks, LoadBalancers
from diagrams.azure.security import KeyVaults
from diagrams.azure.management import Policies
from diagrams.azure.monitor import LogAnalyticsWorkspaces

with Diagram("Azure Landing Zone High-Level", show=False, filename="landingzone-highlevel"):
    with Cluster("Management Group Hierarchy"):
        mgmt = Policy("Policy & Governance")

    with Cluster("Connectivity Layer"):
        hub = VirtualNetworks("Hub VNet")
        spoke = VirtualNetworks("Spoke VNet")
        lb = LoadBalancers("Load Balancer")

    with Cluster("Identity Layer"):
        kv = KeyVaults("Key Vault")

    with Cluster("Monitoring Layer"):
        log = LogAnalyticsWorkspaces("Log Analytics")

    mgmt >> hub >> spoke >> kv >> log
