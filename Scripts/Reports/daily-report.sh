#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H-%M")
REPORT_DIR=~/BBB/Business/Reports
REPORT_FILE="$REPORT_DIR/bbb-daily-report-$DATE.txt"

mkdir -p "$REPORT_DIR"

{
echo "===== BIGBRAINBRAND DAILY OPS REPORT ====="
echo "Date: $(date)"
echo ""
echo "===== ADMIN VM ====="
hostname
uptime
free -h
df -h /
echo ""
echo "===== EPYC HOST ====="
ssh epyc "hostname; uptime; free -h; df -h /"
echo ""
echo "===== VM STATUS ====="
ssh epyc "virsh list --all"
echo ""
echo "===== SERVICES ====="
~/BBB/Scripts/Alerts/check-services.sh
echo ""
echo "===== OLLAMA MODELS ====="
curl -s http://192.168.0.101:11434/api/tags | jq '.models[].name'
} > "$REPORT_FILE"

echo "Report created:"
echo "$REPORT_FILE"
