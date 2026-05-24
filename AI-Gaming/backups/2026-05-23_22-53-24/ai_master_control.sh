#!/bin/bash

while true; do
  clear

  echo "====================================="
  echo "      BBB AI GAMING CONTROL"
  echo "====================================="
  echo ""
  echo "1) Start AI Spectator"
  echo "2) Start Voice Spectator"
  echo "3) Start Highlight Detector"
  echo "4) Generate Highlight Report"
  echo "5) Generate Stream Titles"
  echo "6) Generate Content Pack"
  echo "7) Run Full Auto Pipeline"
  echo "8) View System Status"
  echo "9) Exit"
  echo ""

  read -p "Select Option: " CHOICE

  case $CHOICE in

    1)
      export DISPLAY=:0
      python3 game_vision.py
      ;;

    2)
      export DISPLAY=:0
      python3 ai_spectator_voice.py
      ;;

    3)
      python3 ai_event_detector.py
      ;;

    4)
      python3 ai_highlight_report.py
      ;;

    5)
      python3 ai_stream_titles.py
      ;;

    6)
      python3 ai_content_pack.py
      ;;

    7)
      ./ai_auto_pipeline.sh
      ;;

    8)
      ./ai_gaming_status.sh
      ;;

    9)
      exit
      ;;

    *)
      echo ""
      echo "Invalid option."
      sleep 2
      ;;
  esac

  echo ""
  read -p "Press ENTER to continue..."
done
