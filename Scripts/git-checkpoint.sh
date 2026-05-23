#!/bin/bash

cd ~/BBB || exit

echo "===== BBB GIT STATUS ====="
git status

echo ""
read -p "Commit message: " MSG

git add .
git commit -m "$MSG"
