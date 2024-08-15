#!/bin/bash

export PATH="$(pwd)/venv/bin:$PATH"
echo "env_run"
python bonds_stats.py
