#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

mkdir -p backups/$TIMESTAMP

cp -r *.py backups/$TIMESTAMP/ 2>/dev/null
cp -r *.sh backups/$TIMESTAMP/ 2>/dev/null
cp -r *.md backups/$TIMESTAMP/ 2>/dev/null
cp -r branding backups/$TIMESTAMP/ 2>/dev/null
cp -r web backups/$TIMESTAMP/ 2>/dev/null

echo ""
echo "BBB AI Backup Created:"
echo "backups/$TIMESTAMP"
echo ""
