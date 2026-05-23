#!/bin/bash

VRAM_USED=$(ssh epyc "nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits" | head -n 1)
GPU_UTIL=$(ssh epyc "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits" | head -n 1)

GAMING_STATE=$(ssh epyc "virsh domstate gaming 2>/dev/null")
MEDIA_STATE=$(ssh epyc "virsh domstate media-creation 2>/dev/null")
DEV_STATE=$(ssh epyc "virsh domstate dev-suite 2>/dev/null")

echo "===== BBB GPU RENTAL CHECK ====="
echo "VRAM Used: ${VRAM_USED} MiB"
echo "GPU Util: ${GPU_UTIL}%"
echo "Gaming VM: $GAMING_STATE"
echo "Media VM: $MEDIA_STATE"
echo "Dev VM: $DEV_STATE"
echo ""

if [ "$GAMING_STATE" = "running" ] || [ "$MEDIA_STATE" = "running" ]; then
  echo "Rental Status: HOLD"
  echo "Reason: Premium VM is running."
  exit 1
fi

if [ "$VRAM_USED" -lt 2000 ] && [ "$GPU_UTIL" -lt 20 ]; then
  echo "Rental Status: OK"
  echo "Reason: GPU appears idle."
else
  echo "Rental Status: HOLD"
  echo "Reason: GPU is currently in use."
fi
