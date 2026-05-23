# BBB Daily Operator Routine

## Morning Startup
1. SSH into admin-vm
2. Run:
   start-bbb
3. Check:
   - dashboards
   - VM status
   - service health
   - storage
   - backups

---

## Daily Commands

Health:
health

Services:
services-check

VM Control:
vm list

Dashboards:
dashboards

Backup:
backup-bbb

Checkpoint:
checkpoint

Report:
report

Notes:
note

---

## Before Major Changes
- Create VM snapshot
- Run backup-bbb
- Commit Git checkpoint

---

## Before Customer Deployment
- Verify lockdown checklist
- Verify monitoring
- Verify backups
- Create clean snapshot

---

## End of Day
1. Run report
2. Add important notes
3. Run checkpoint
4. Verify backups exist

