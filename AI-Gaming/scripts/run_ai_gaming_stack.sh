#!/bin/bash

cd ~/BBB/AI-Gaming
source venv/bin/activate

echo "Starting BBB AI Gaming Stack..."

pkill -f spectator_dashboard.py
pkill -f dashboard_server.py

nohup python3 spectator_dashboard.py > spectator_dashboard.log 2>&1 &
nohup python3 dashboard_server.py > summary_dashboard.log 2>&1 &

echo ""
echo "Dashboards:"
echo "Spectator Logs: http://192.168.0.102:5090"
echo "Session Summary: http://192.168.0.102:5091"
echo ""
