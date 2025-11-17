
---

# 📁 **docs/design-decisions.md**

```markdown
# Design Decisions – Azure Landing Zone

This document explains the rationale behind the architecture and implementation choices made in this landing zone.

---

## 1. Why Hub & Spoke?

- Centralized security boundary  
- Simplified hybrid connectivity (VPN/ExpressRoute)  
- Shared services (firewall, DNS, Bastion) live in the hub  
- Spokes remain lightweight and workload-specific  

Hub & spoke is a CAF-recommended baseline for enterprises.

---

## 2. Why Use Management Groups?

- Clear separation of governance layers  
- Consistent tagging, policies, and RBAC  
- Enables scalable multi-environment structure  
- Allows for multi-business-unit expansion  

---

## 3. Why Policy-as-Code?

Reasons:

1. **Consistency** – workloads comply automatically  
2. **Security by default** – HTTPS-only, allowed locations  
3. **Governance enforcement** – tagging standards  
4. **Automated remediation** with DINE (DeployIfNotExists)

Policies selected match real enterprise standards.

---

## 4. Why Log Analytics + Automation?

- Centralized monitoring  
- Native integration with Defender and Sentinel  
- Supports Update Management and alert automation  
- Aligns with Microsoft’s Management landing zone pattern  

---

## 5. Why Terraform?

- Modular, scalable IaC  
- Supports management groups + policy resources  
- Easily integrates with CI/CD  
- Remote backend with locking prevents concurrency issues  

---

## 6. Why Remote State in Storage Account?

Reasons:

- Simple and Azure-native  
- Supports locking  
- No cost  
- Ideal for enterprise pipelines where Terraform Cloud is not allowed  

---

## 7. Why the CI/CD Structure?

- PR Validation prevents broken code from merging  
- Gated apply ensures controlled production deployments  
- Destroy pipeline supports full rebuild testing  
- Clear separation mirrors real enterprise environments  

---

## 8. Future Design Enhancements

- Add GitHub Actions with OIDC  
- Add Sentinel or Conftest for policy enforcement in CI  
- Integrate Azure Monitor Workbooks  
- Add architecture test suite (Terratest or Checkov)  
- Add multi-region failover hub  

These improvements help scale toward a multi-region enterprise landing zone.

