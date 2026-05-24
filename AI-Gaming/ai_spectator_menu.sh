#!/bin/bash

while true; do
  clear
  echo "===== BBB AI GAMING SPECTATOR ====="
  echo ""
  echo "1) Run vision only"
  echo "2) Run vision + voice"
  echo "3) Run vision + voice + logs"
  echo "4) View latest logs"
  echo "5) Exit"
  echo ""

  read -p "Choose option: " CHOICE

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
      export DISPLAY=:0
      python3 ai_spectator_logs.py
      ;;
    4)
      ls -lt spectator-logs | head -20
      ;;
    5)
      exit
      ;;
    *)
      echo "Invalid option."
      sleep 2
      ;;
  esac
done
