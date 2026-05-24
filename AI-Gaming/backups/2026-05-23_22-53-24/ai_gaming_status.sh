#!/bin/bash

echo "===== BBB AI GAMING STACK STATUS ====="
echo ""

echo "Processes:"
ps aux | grep -Ei "spectator_dashboard|dashboard_server|ai_spectator|game_vision" | grep -v grep

echo ""
echo "Ports:"
ss -tulnp | grep -E "5090|5091" || echo "No AI gaming dashboard ports active."

echo ""
echo "Dashboards:"
echo "Spectator Logs:  http://192.168.0.102:5090"
echo "Session Summary: http://192.168.0.102:5091"

echo ""
echo "Latest Captures:"
ls -lt spectator-logs 2>/dev/null | head -10
