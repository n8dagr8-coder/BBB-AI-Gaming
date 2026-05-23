#!/bin/bash

echo "===== BBB GPU STATUS ====="
echo ""

ssh epyc "nvidia-smi"

echo ""
echo "===== GPU RENTAL READINESS ====="

VRAM_USED=$(ssh epyc "nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits" | head -n 1)

echo "VRAM Used: ${VRAM_USED} MiB"

if [ "$VRAM_USED" -lt 2000 ]; then
  echo "Status: GPU appears mostly idle"
  echo "Rental Readiness: POSSIBLE"
else
  echo "Status: GPU currently in use"
  echo "Rental Readiness: HOLD"
fi
