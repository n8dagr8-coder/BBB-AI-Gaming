#!/bin/bash

echo "===== BBB VM STATUS ====="
echo ""

virsh list --all

echo ""
echo "===== SYSTEM LOAD ====="
uptime

echo ""
echo "===== MEMORY ====="
free -h

echo ""
echo "===== STORAGE ====="
df -h /

echo ""
echo "===== OLLAMA ====="
curl -s http://192.168.0.101:11434/api/tags | jq '.models[].name'
