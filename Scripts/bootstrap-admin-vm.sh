#!/bin/bash

echo "===== BBB ADMIN VM BOOTSTRAP ====="

sudo apt update && sudo apt upgrade -y

sudo apt install -y \
curl wget git unzip zip p7zip-full \
htop btop tmux fastfetch \
neovim tree jq \
python3 python3-pip python3-venv \
docker.io docker-compose \
openssh-server \
flatpak \
net-tools dnsutils \
build-essential

echo ""
echo "===== INSTALL COMPLETE ====="
