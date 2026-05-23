#!/bin/bash

echo "===== BBB HEALTH CHECK ====="
echo ""

echo "ADMIN VM:"
hostname
uptime
free -h
df -h /

echo ""
echo "EPYC HOST:"
ssh epyc "hostname; uptime; free -h; df -h /"

echo ""
echo "VM STATUS:"
ssh epyc "virsh list --all"

echo ""
echo "CORE SERVICES:"
for port in 3000 3001 5678 9090 9443 11434; do
  timeout 3 bash -c "cat < /dev/null > /dev/tcp/192.168.0.101/$port" \
    && echo "Port $port: UP" \
    || echo "Port $port: DOWN"
done

echo ""
echo "OLLAMA MODELS:"
curl -s http://192.168.0.101:11434/api/tags | jq '.models[].name'
