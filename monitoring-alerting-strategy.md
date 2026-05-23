# BBB Monitoring and Alerting Strategy

## Goal
Detect infrastructure problems early and respond before outages escalate.

---

## Core Monitoring Stack

### Grafana
Purpose:
- dashboards
- metrics visualization
- historical tracking

### Prometheus
Purpose:
- metrics collection
- service monitoring
- infrastructure scraping

### BBB Scripts
Purpose:
- quick health checks
- operational reports
- service validation

---

## What Must Be Monitored

### Infrastructure
- CPU usage
- RAM usage
- disk usage
- temperature
- uptime
- network usage

### VM Layer
- VM running state
- VM resource pressure
- snapshot existence
- backup success

### AI Layer
- Ollama availability
- GPU usage
- model responsiveness
- inference failures

### Services
- Portainer
- Grafana
- Open WebUI
- n8n
- Prometheus

---

## Alert Priorities

### Critical
- host offline
- disk full
- VM failure
- backup failure

### Warning
- high RAM
- high CPU
- service restart
- excessive storage growth

### Informational
- completed backups
- successful snapshots
- provisioning events

---

## Future Alert Channels

Planned:
- Discord webhook
- Telegram
- Email
- mobile push alerts

---

## Golden Rule

If it matters:
monitor it.

If it can fail:
alert on it.
