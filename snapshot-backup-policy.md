# BBB Snapshot and Backup Policy

## Snapshot Rules

Snapshots are taken only:
- after stable milestones
- before risky changes
- before tenant handoff
- before major updates
- before lockdown changes

Avoid random snapshots during active troubleshooting unless rollback risk is high.

---

## VM Snapshot Names

Use clear names:

admin-vm:
- post-ai-stack
- post-full-admin-ai-gui
- pre-major-update

office-vm:
- clean-office-baseline
- pre-lockdown
- client-ready

dev-vm:
- clean-dev-baseline
- pre-tooling-change
- client-ready

media-vm:
- clean-media-baseline
- pre-creative-stack-change

gaming-vm:
- clean-gaming-baseline
- pre-driver-update

---

## Backup Rules

Important data should live in:
- ~/BBB
- ~/BBB/Business
- ~/BBB/Docs
- ~/BBB/Scripts
- ~/BBB/Backups

Run manual backup:
backup-bbb

Run restore:
restore-bbb

---

## Golden Rule

Snapshot protects VM state.
Backup protects files.
Git protects scripts/docs/configs.

Use all three.
