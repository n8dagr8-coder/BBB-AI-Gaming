# BBB GPU Operational Thresholds

## GPU Owner Priority

Priority Order:

1. admin infrastructure
2. media production
3. gaming sessions
4. development CUDA work
5. external rental

---

## Rental Eligibility

Rental allowed only if:
- gaming VM OFF
- media VM OFF
- VRAM usage under 2GB
- GPU utilization low
- no active rendering jobs
- no internal AI queue

---

## Office VM Policy

Office VM:
- never receives passthrough
- uses remote/shared AI only

---

## Dev VM Policy

Dev VM:
- temporary passthrough only
- preferably remote inference

---

## Gaming VM Policy

Gaming VM:
- temporary passthrough allowed
- must release GPU afterward

---

## Media VM Policy

Media VM:
- temporary passthrough allowed
- highest GPU priority after admin infrastructure

---

## Host Protection Rule

The EPYC host must always retain enough GPU access for:
- Ollama
- ComfyUI
- monitoring
- infrastructure AI

---

## Golden Rule

Revenue workloads must never destabilize infrastructure.
