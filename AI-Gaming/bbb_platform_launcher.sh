#!/bin/bash

while true; do
  clear

  cat branding/bbb-banner.txt

  echo ""
  echo "========================================"
  echo "        BBB PLATFORM CONTROL"
  echo "========================================"
  echo ""
  echo "1) Launch BBB AI Gaming"
  echo "2) View System Report"
  echo "3) Run Auto Pipeline"
  echo "4) Start Highlight Dashboard"
  echo "5) Start Summary Dashboard"
  echo "6) Backup BBB Platform"
  echo "7) View GPU Status"
  echo "8) View VM Status"
  echo "9) Exit"
  echo ""

  read -p "Choose Option: " OPTION

  case $OPTION in

    1)
      ./bbb_boot_sequence.sh
      ;;

    2)
      ./bbb_system_report.sh
      ;;

    3)
      ./ai_auto_pipeline.sh
      ;;

    4)
      python3 highlight_dashboard.py
      ;;

    5)
      python3 highlight_report_server.py
      ;;

    6)
      ./backup_bbb_ai.sh
      ;;

    7)
      nvidia-smi
      ;;

    8)
      virsh list --all
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
