#!/bin/bash

echo "🔥 [1] Running DNS Attacks..."
python3 main.py --dns local

echo "⚔️ [2] Running STRIKE Mode (smart scan + exploit)..."
python3 main.py --strike --stealth

echo "🧨 [3] Running STRIKE UNCHAINED Mode (fallback probes)..."
python3 main.py --strike-unchained

echo "🤖 [4] Running ADAPTIVE AI STRIKE Mode..."
python3 main.py --adaptive-ai --stealth
