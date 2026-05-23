# BBB Incident Response Playbook

## Goal
Respond to outages and failures calmly, consistently, and recoverably.

---

## First Rule
Do NOT panic-change multiple systems at once.

Change one thing at a time.

---

## Initial Response Checklist

1. Identify:
- VM issue?
- Network issue?
- Service issue?
- Disk issue?
- GPU issue?
- User issue?

2. Verify:
health

3. Verify services:
services-check

4. Verify VMs:
vm list

5. Verify dashboards:
dashboards

---

## Before Risky Changes
- Create snapshot
- Run backup-bbb
- Run checkpoint

---

## If VM Fails
1. Check:
vm list

2. Attempt graceful reboot:
vm reboot VMNAME

3. If frozen:
vm force-stop VMNAME
vm start VMNAME

4. Verify SSH
5. Verify RustDesk
6. Verify storage

---

## If Ollama Fails
1. Verify:
curl http://192.168.0.101:11434/api/tags

2. Verify service ports
3. Verify EPYC load
4. Verify GPU usage

---

## If Dashboards Fail
Check:
- Docker
- Port mappings
- Reverse proxy
- Service containers

---

## Recovery Priority
1. Infrastructure
2. Backups
3. Networking
4. Admin VM
5. Monitoring
6. Customer systems
7. AI services

---

## Golden Rule
Slow is smooth.
Smooth is fast.
