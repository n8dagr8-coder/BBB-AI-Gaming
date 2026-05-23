# BBB GPU Allocation Strategy

## Core Rule
The RTX 6000 remains owned by the EPYC host by default.

Do NOT permanently dedicate the GPU to low-value VMs.

## Default GPU Owner
EPYC host:
- Ollama
- ComfyUI
- AI inference
- shared AI services
- future GPU rentals

## Office VM
- no passthrough
- light AI only through Open WebUI / browser access

## Gaming VM
- temporary passthrough allowed
- premium gaming/streaming use
- release GPU afterward

## Media VM
- temporary passthrough allowed
- AI media and rendering sessions

## Dev VM
- remote inference preferred
- temporary passthrough only for CUDA/dev needs

## Rental System
Future goal:
- detect idle GPU
- check VRAM usage
- allow rental only when internal workloads are idle

## Golden Rule
Shared host inference scales better than permanent passthrough.
