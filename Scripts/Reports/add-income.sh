#!/bin/bash

CSV=~/BBB/Business/Income/income-tracker.csv

read -p "Client: " CLIENT
read -p "Service: " SERVICE
read -p "Tier: " TIER
read -p "VM: " VM
read -p "Amount: " AMOUNT
read -p "Status: " STATUS
read -p "Payment Method: " METHOD
read -p "Notes: " NOTES

DATE=$(date +"%Y-%m-%d")

echo "$DATE,$CLIENT,$SERVICE,$TIER,$VM,$AMOUNT,$STATUS,$METHOD,$NOTES" >> "$CSV"

echo ""
echo "Income entry added to:"
echo "$CSV"
