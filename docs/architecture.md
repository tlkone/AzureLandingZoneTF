# Azure Landing Zone – Architecture Overview

This document provides a detailed view of the architecture implemented in this landing zone. The design follows the Microsoft Cloud Adoption Framework (CAF) and implements a production-ready hub & spoke environment with centralized governance, networking, and security controls.

---

## 1. Management Group Hierarchy

The environment is structured into multiple Management Groups (MGs) to align with CAF and provide clean separation of duties:

<pre>
Tenant Root Group
│
├── Platform (MG)
│   ├── Identity (MG)
│   ├── Management (MG)
│   └── Connectivity (MG)
│
└── Landing Zones (MG)
    ├── Corp (MG)
    └── Sandbox (MG)
</pre>

### Purpose of each MG:

- **Identity**  
  Hosts Key Vault and Managed Identities used by platform services.

- **Management**  
  Hosts Log Analytics workspace and Automation Account.

- **Connectivity**  
  Hosts the Hub VNet, Azure Firewall, Bastion, and VPN Gateway.

- **Landing Zones (Corp / Sandbox)**  
  Where workloads and applications are deployed.

---

## 2. Network Topology (Hub & Spoke)

A classic enterprise-ready **hub & spoke** topology:

- **Hub VNet** (`10.0.0.0/16`)  
  - Azure Firewall  
  - VPN Gateway  
  - Bastion Host  
  - Shared DNS / routing

- **Spoke 1** (`10.10.0.0/16`)  
- **Spoke 2** (`10.20.0.0/16`)  
- **Spoke 3** (`10.30.0.0/16`)  

### Key Networking Features

- **Gateway transit enabled**
- **VNet peering with "use remote gateway" on spokes**
- **Centralized inspection via Azure Firewall**
- **Forwarded traffic enabled**

---

## 3. Shared Platform Services

### Logging & Monitoring
- Log Analytics workspace
- Automation Account (Update schedules, hybrid jobs)

### Identity
- Centralized Key Vault
- System-assigned / user-assigned Managed Identities

### Security
- Azure Firewall with default route pointers
- Microsoft Defender plans (DeployIfNotExists)

---

## 4. Policy-as-Code

Policies enforced at Platform & Landing Zone scope:

- Allowed locations → `eastus`, `centralus`
- Enforce HTTPS on Storage
- Require `costCenter` tag
- Key Vault Soft Delete (DINE)
- Defender for Servers / Key Vault (DINE)
- VM backup policy (optional)

Compliance results routed to Log Analytics.

---

## 5. Remote State Architecture

Terraform backend uses:

- Resource Group: `tfstate-rg`
- Storage Account: `tfstatestorageXXXX`
- Container: `tfstate`
- Key: `landingzone/dev.tfstate`

Configured via `backend.tf`.

---

## 6. High-Level Diagram

<details>
  <summary>📊 View Interactive Architecture Diagram</summary>

  <!-- GitHub Pages interactive diagram -->
  <p>
    👉 Open the interactive diagram here:  
    <a href="https://tlkone.github.io/Azurearchitecturediagram/" target="_blank">
      https://tlkone.github.io/Azurearchitecturediagram/
    </a>
  </p>

</details>


---

## 7. Architecture Strengths

- Enterprise-grade governance
- Centralized security boundary
- Separation of concerns through MG structure
- Reusable modular Terraform code
- Full policy compliance & auditing

