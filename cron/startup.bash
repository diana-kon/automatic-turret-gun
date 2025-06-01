#!/bin/bash
cd $(dirname "$0")
cd ..
echo "update"
git pull
echo "run"
source .venv/bin/activate
./src/main.py
deactivate
echo "repeat"
cd cron
./startup.bash
