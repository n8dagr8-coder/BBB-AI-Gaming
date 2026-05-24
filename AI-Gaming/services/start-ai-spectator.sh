#!/bin/bash

export DISPLAY=:0

cd ~/BBB/AI-Gaming
source venv/bin/activate

python3 ai_spectator_logs.py
