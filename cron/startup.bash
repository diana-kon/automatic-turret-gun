#!/bin/bash
cd $(dirname "$0")
cd ..
echo "update"
git pull
echo "run"
./src/main.py
echo "repeat"
cd cron
./startup.bash
