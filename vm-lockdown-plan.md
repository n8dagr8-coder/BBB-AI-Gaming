# BBB VM Lockdown Plan

## Goal
Prepare VMs for tiered business use with controlled access, limited apps, and tenant isolation.

## Core Rule
Customers should receive controlled workspaces, not open PCs.

---

## Light Tier
Target VM:
- office-vm

Allowed:
- Browser
- Office apps
- PDF tools
- AI shortcut portal

Blocked:
- Admin rights
- App installs
- Docker
- PowerShell admin
- Registry editing
- Host/network discovery

---

## Dev Tier
Target VM:
- dev-vm

Allowed:
- VS Code
- Git
- Browser
- Approved language runtimes
- Limited SSH

Blocked:
- Host access
- Privileged Docker
- Unauthorized service hosting
- Tenant-to-tenant access

---

## Media Tier
Target VM:
- media-vm

Allowed:
- Creative apps
- AI media tools
- Approved asset folders

Blocked:
- Admin rights
- System changes
- Unapproved downloads
- External credential storage

---

## Gaming Tier
Target VM:
- gaming-vm

Allowed:
- Steam
- Approved games
- Streaming client

Blocked:
- Admin rights
- Crypto mining
- Cheats/trainers
- Host access
- Unapproved installs

---

## Internal Only
Target VM:
- admin-vm

Rules:
- Never rent
- Password manager allowed
- SSH keys allowed
- Infrastructure dashboards allowed
- Business credentials allowed

---

## Hardening Checklist
- [ ] Static IP
- [ ] SSH verified
- [ ] RustDesk verified
- [ ] Non-admin tenant user
- [ ] Admin account separated
- [ ] App list finalized
- [ ] Snapshot before handoff
- [ ] Backup policy assigned
- [ ] Monitoring enabled
- [ ] Notes added to client folder
