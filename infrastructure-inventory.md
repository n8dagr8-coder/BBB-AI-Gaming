# BBB Infrastructure Inventory

## Host Systems

### EPYC Main Host
IP: 192.168.0.101
Purpose:
- Ollama
- Docker
- VM Host
- AI inference
- Infrastructure backbone

### admin-vm
IP: 192.168.0.102
Purpose:
- Operations
- Monitoring
- Automation
- AI coding
- Dashboard management

### media-vm
IP: 192.168.0.103
Purpose:
- Media workflows
- AI video
- Editing

### gaming-vm
IP: 192.168.0.104
Purpose:
- Gaming
- Streaming
- Testing

### dev-vm
IP: 192.168.0.105
Purpose:
- Development
- Code testing
- Sandboxes

### office-vm
IP: 192.168.0.106
Purpose:
- Business
- Office tasks
- Light client workloads

---

## Core Services

Portainer:
https://192.168.0.101:9443

Grafana:
http://192.168.0.101:3001

Open WebUI:
http://192.168.0.101:3000

n8n:
http://192.168.0.101:5678

Prometheus:
http://192.168.0.101:9090

Ollama:
http://192.168.0.101:11434

---

## Critical Standards

Desktop:
- XFCE
- X11
- lightdm

Remote Access:
- RustDesk
- SSH

Snapshots:
- post-ai-stack
- post-full-admin-ai-gui
