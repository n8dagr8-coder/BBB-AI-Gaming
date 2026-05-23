#!/bin/bash

echo "Starting BBB Workspace..."

# Open dashboards
~/BBB/Scripts/Monitoring/open-dashboards.sh &

# Start tmux session
tmuxinator start bbb

