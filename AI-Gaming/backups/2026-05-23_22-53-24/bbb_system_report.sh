#!/bin/bash

clear

cat branding/bbb-banner.txt

echo ""
echo "========== BBB SYSTEM REPORT =========="
echo ""

echo "Hostname:"
hostname

echo ""
echo "Current User:"
whoami

echo ""
echo "GPU Status:"
nvidia-smi --query-gpu=name,temperature.gpu,memory.used,memory.total,utilization.gpu --format=csv

echo ""
echo "RAM Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h /

echo ""
echo "AI Processes:"
ps aux | grep -Ei "ollama|python|spectator|dashboard" | grep -v grep

echo ""
echo "VM Status:"
virsh list --all

echo ""
echo "Open AI Ports:"
ss -tulnp | grep -E "11434|5090|5091|5092|5093"

echo ""
echo "======================================="
echo " BBB AI GAMING INFRASTRUCTURE ONLINE"
echo "======================================="
