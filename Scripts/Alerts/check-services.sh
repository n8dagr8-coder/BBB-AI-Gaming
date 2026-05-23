#!/bin/bash

SERVICES=(
  "3000 OpenWebUI"
  "3001 Grafana"
  "5678 n8n"
  "9090 Prometheus"
  "9443 Portainer"
  "11434 Ollama"
)

echo "===== BBB SERVICE CHECK ====="

for item in "${SERVICES[@]}"; do
  PORT=$(echo $item | awk '{print $1}')
  NAME=$(echo $item | awk '{print $2}')

  timeout 2 bash -c "cat < /dev/null > /dev/tcp/192.168.0.101/$PORT" 2>/dev/null

  if [ $? -eq 0 ]; then
    echo "[UP]   $NAME ($PORT)"
  else
    echo "[DOWN] $NAME ($PORT)"
  fi
done
