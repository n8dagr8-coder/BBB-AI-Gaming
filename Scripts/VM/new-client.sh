#!/bin/bash

read -p "Client Name: " CLIENT

DIR=~/BBB/Business/Clients/$CLIENT

mkdir -p "$DIR"

cp ~/BBB/Templates/client-vm-template.txt "$DIR/info.txt"

echo ""
echo "Client workspace created:"
echo "$DIR"
