# BBB Golden VM Template Plan

## Goal
Create reusable clean VM baselines for rapid deployment.

---

## Golden Templates

### admin-vm-template
Purpose:
- infrastructure operations
- monitoring
- automation
- AI coding

Includes:
- XFCE
- lightdm
- X11
- RustDesk
- VS Code
- Continue
- Aider
- Brave
- tmux
- BBB scripts

Never rented.

---

### office-vm-template
Purpose:
- business productivity
- lightweight tenant use

Includes:
- Browser
- Office tools
- PDF tools
- AI portal access

Locked down.

---

### dev-vm-template
Purpose:
- coding
- development
- sandboxing

Includes:
- VS Code
- Git
- SSH tools
- runtimes

Restricted host access.

---

### media-vm-template
Purpose:
- AI media
- creative workflows
- editing

Includes:
- media apps
- AI tools
- storage mounts

GPU optional.

---

### gaming-vm-template
Purpose:
- gaming
- streaming
- testing

Includes:
- Steam
- GPU drivers
- streaming apps

Strict restrictions.

---

## Golden Template Rules

Before template creation:
- fully updated
- health verified
- snapshot created
- backup verified
- scripts installed
- monitoring verified

After template finalized:
- create clean snapshot
- mark as GOLDEN
- never modify directly

Clone from template instead.

