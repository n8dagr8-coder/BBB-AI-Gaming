#!/bin/bash

echo "Stopping BBB AI Gaming services..."

pkill -f game_vision || true
pkill -f ai_spectator || true
pkill -f spectator_dashboard || true
pkill -f dashboard_server || true
pkill -f highlight_dashboard || true
pkill -f highlight_report_server || true
pkill -f ai_clip_queue || true
pkill -f ai_event_detector || true
pkill -f ai_hype_meter || true

echo "Stopped."
