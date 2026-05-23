# BBB Tenant Isolation Roadmap

## Goal
Make rented/loaned VMs safe, controlled, and tier-based.

---

## Core Rule
Customers get controlled workspaces, not unrestricted computers.

---

## Phase 1 — Basic Controls
- Non-admin tenant account
- Separate admin account
- Disable sudo/admin rights
- Restrict app installs
- Limit allowed apps
- Create clean snapshot before handoff

---

## Phase 2 — Network Controls
- Static IP reservations
- Separate VLANs later
- Block tenant-to-tenant access
- Restrict LAN discovery
- Only allow required services
- Monitor bandwidth

---

## Phase 3 — Resource Controls
- vCPU limits
- RAM limits
- disk quotas
- GPU access only by tier
- no crypto mining
- no unauthorized service hosting

---

## Phase 4 — App Control
- Browser only for Light Tier
- Approved apps only
- No random downloads
- No Docker unless Dev Tier
- No privileged containers

---

## Phase 5 — Business Controls
- Client folder created
- Tier recorded
- Billing recorded
- Backup policy assigned
- Support notes tracked
- Snapshot before handoff

---

## Internal-Only Systems
admin-vm is never rented.
It remains the trusted operations zone.

