#!/bin/bash

while true; do
    clear

    echo "=================================="
    echo "   BIGBRAINBRAND OPERATOR MENU"
    echo "=================================="
    echo ""
    echo "1) Health Check"
    echo "2) VM List"
    echo "3) Open Dashboards"
    echo "4) Backup BBB"
    echo "5) Services Check"
    echo "6) Daily Report"
    echo "7) Exit"
    echo ""

    read -p "Choose option: " CHOICE

    case $CHOICE in
        1)
            ~/BBB/Scripts/Monitoring/bbb-health.sh
            ;;
        2)
            ~/BBB/Scripts/VM/vm-control.sh list
            ;;
        3)
            ~/BBB/Scripts/Monitoring/open-dashboards.sh
            ;;
        4)
            ~/BBB/Scripts/Backups/backup-bbb.sh
            ;;
        5)
            ~/BBB/Scripts/Alerts/check-services.sh
            ;;
        6)
            ~/BBB/Scripts/Reports/daily-report.sh
            ;;
        7)
            exit
            ;;
        *)
            echo "Invalid option."
            ;;
    esac

    echo ""
    read -p "Press ENTER to continue..."
done
