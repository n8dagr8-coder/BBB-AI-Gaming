#!/bin/bash
cd ~/BBB/Apps/vm-control
source venv/bin/activate
pkill -f "python3 app.py" || true
python3 app.py
