# BBB Configuration Standards

## Linux Standard

Preferred:
- Ubuntu LTS

Desktop:
- XFCE

Display:
- X11

Display Manager:
- lightdm

Avoid:
- Wayland

---

## Remote Access

Primary:
- RustDesk

Secondary:
- SSH

Trusted Operator Device:
- Terminus on phone

---

## Browser Standard

Preferred:
- Brave

Profiles:
- BBB Admin
- BBB Business
- BBB Dev
- BBB Media

---

## AI Stack Standard

Primary:
- Ollama

Coding:
- Continue
- Aider
- VS Code

---

## VM Naming Standard

Examples:
- admin-vm
- office-vm
- dev-vm
- media-vm
- gaming-vm

---

## IP Standard

EPYC Host:
192.168.0.101

admin-vm:
192.168.0.102

media-vm:
192.168.0.103

gaming-vm:
192.168.0.104

dev-vm:
192.168.0.105

office-vm:
192.168.0.106

---

## Snapshot Standard

Use meaningful names:
- post-ai-stack
- clean-office-baseline
- pre-major-update

Never use:
- snapshot1
- test2
- random names

---

## Golden Rule

Standardize first.
Automate second.
Scale third.
