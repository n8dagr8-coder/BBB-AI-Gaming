# Admin VM Rebuild Guide

## Purpose
Rebuild the BigBrainBrand Admin VM quickly if it breaks.

## Static IP
192.168.0.102

## Required Base
- Ubuntu
- XFCE
- lightdm
- X11
- SSH
- RustDesk
- Brave
- VS Code
- Aider
- Continue
- Docker tools

## Core Commands

SSH:
ssh admin

Health:
health

VM Control:
vm list

Dashboards:
dashboards

Backup:
backup-bbb

Restore:
restore-bbb

Checkpoint:
checkpoint

## Critical Rule
Use XFCE + lightdm + X11.
Do NOT use Wayland.

## RustDesk
ID Server:
192.168.0.101

Key:
jBlGzcO0jivSTo8qv5YXIP8QQVNEN964cUWqq3SVuVs=

## Ollama API
http://192.168.0.101:11434

## Models
qwen2.5-coder:7b
llama3.1:8b
