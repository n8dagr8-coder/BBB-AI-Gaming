# BigBrainBrand EPYC Homelab Session Summary

## Current Architecture

EPYC Host:
- IP: 192.168.0.101
- Role: VM host, Ollama, Docker services, AI compute

Admin VM:
- IP: 192.168.0.102
- Role: trusted operator workstation
- Access: ssh admin
- RustDesk working
- XFCE + lightdm + X11

VMs:
- media-vm: 192.168.0.103
- gaming-vm: 192.168.0.104
- dev-vm: 192.168.0.105
- office-vm: 192.168.0.106

## Core Commands

ssh admin
health
services-check
vm list
dashboards
backup-bbb
restore-bbb
checkpoint
report
note
start-bbb
ops

## AI Stack

Ollama:
http://192.168.0.101:11434

Models:
- qwen2.5-coder:7b
- llama3.1:8b

Tools:
- Aider working
- VS Code working
- Continue configured
- Open WebUI working

## Critical Lessons

Linux VM standard:
- XFCE
- lightdm
- X11
- NOT Wayland

Workflow standard:
Phone → Terminus → EPYC → admin-vm

Trusted zone:
admin-vm only for credentials, dashboards, password manager, automation, and infrastructure control.

## Snapshots

admin-vm:
- post-ai-stack
- post-full-admin-ai-gui

## Next Priorities

1. Finish admin-vm function layer
2. Build income/client tracking deeper
3. Create VM lockdown scripts
4. Build golden VM templates
5. Add GitHub remote backup
6. Add Vaultwarden/Bitwarden workflow
7. Start tenant-ready deployment system
