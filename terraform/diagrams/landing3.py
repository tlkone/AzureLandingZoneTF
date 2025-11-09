from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.azure.analytics import LogAnalyticsWorkspaces
from diagrams.azure.network import VirtualNetworkClassic, Subnets
from diagrams.azure.security import KeyVaults

# Style
graph_attr = {"bgcolor": "#0b1221", "pad": "0.4", "ranksep": "0.9", "nodesep": "0.7", "splines": "spline"}
node_attr  = {"fontname": "Segoe UI", "color": "#9db4ff", "fontcolor": "#e6ecff"}
edge_attr  = {"color": "#8aa0ff"}

with Diagram(
    "Azure Landing Zone – STRICT (matches current repo)",
    filename="landingzone-highlevel",
    show=False,
    outformat=["png","svg"],
    graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr
):
    # Management & Governance (policy + monitoring)
    with Cluster("Management & Governance"):
        # custom Azure Policy icon (put svg at ./icons/azure-policy.svg)
        try:
            policy = Custom("policy/assignments.tf\n(Policy & Governance)", "./icons/policy.svg")
        except Exception:
            # graceful fallback if icon not found
            policy = Custom("policy/assignments.tf\n(Policy & Governance)", None)
        la = LogAnalyticsWorkspaces("management/loganalytics.tf\n(Log Analytics)")

    # Connectivity: Hub + Spokes (from connectivity/*.tf)
    with Cluster("Platform Subscription (connectivity)"):
        with Cluster("rg-connectivity"):
            hub_vnet = VirtualNetworkClassic("hub.tf → Hub VNet")
            hub_snet = Subnets("hub subnets")

    with Cluster("LZ Subscription – App1 (spoke)"):
        with Cluster("rg-app1"):
            spoke1_vnet = VirtualNetworkClassic("spoke.tf → Spoke VNet (App1)")
            spoke1_snet = Subnets("spoke subnets")

    with Cluster("LZ Subscription – App2 (spoke)"):
        with Cluster("rg-app2"):
            spoke2_vnet = VirtualNetworkClassic("spoke.tf → Spoke VNet (App2)")
            spoke2_snet = Subnets("spoke subnets")

    # Identity: Key Vault (from identity/keyvault.tf)
    with Cluster("Identity"):
        kv = KeyVaults("identity/keyvault.tf\n(Key Vault)")

    # Hub/spoke relationships (from peering.tf)
    hub_vnet - Edge(label="peering") - spoke1_vnet
    hub_vnet - Edge(label="peering") - spoke2_vnet

    # Minimal internal edges
    hub_vnet >> hub_snet
    spoke1_vnet >> spoke1_snet
    spoke2_vnet >> spoke2_snet

    # Policies applied + diagnostics to LA
    for v in [hub_vnet, spoke1_vnet, spoke2_vnet]:
        policy >> Edge(label="RBAC / Policy / Tags", color="#ffd166") >> v

    for n in [kv, hub_vnet, spoke1_vnet, spoke2_vnet]:
        n >> Edge(label="diagnostics", color="#74c69d", style="dashed") >> la
