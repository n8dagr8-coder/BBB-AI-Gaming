#!/bin/bash

LOG=~/BBB/Logs/operator-notes.md
DATE=$(date +"%Y-%m-%d %H:%M")

read -p "Note: " NOTE

echo "- [$DATE] $NOTE" >> "$LOG"

echo ""
echo "Note saved to:"
echo "$LOG"
