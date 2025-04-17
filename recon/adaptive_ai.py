# recon/adaptive_ai.py
import random
import time
from recon.intel import full_intel
from exploit.auto_exploit import run_exploit
from main import scan_target

# [🤖] Adaptive AI Strategy Engine
# This module simulates learning by adjusting delay, path, or behavior per target

def adaptive_ai_strike(ip):
    print(f"[🤖 AI] Initiating adaptive strike on {ip}...")
    intel = full_intel(ip)
    print(f"[🧠 INTEL] {intel}")

    # Decide on scan strategy
    delay = random.uniform(0.5, 2.5)
    stealth = intel['WAF'] != 'None'  # Enable stealth if behind WAF
    print(f"[🎭] Stealth Mode: {stealth} | Delay Between Probes: {round(delay,2)}s")

    # Perform smart scan
    ports_services = scan_target(ip, stealth=stealth)
    if not ports_services:
        print("[❌] No services found. Exiting adaptive strike.")
        return

    # Simulate adaptive timing & learning
    time.sleep(delay)

    # Based on CMS/WAF/Cloud, choose smart path
    if intel['CMS'] == 'Wordpress' and 'http' in ports_services.values():
        print("[📦] Target looks like a WordPress site — prioritizing HTTP exploits...")
    elif intel['Cloud'] == 'AWS' and 'http' in ports_services.values():
        print("[☁️] Cloud infra detected — preparing metadata access probes...")

    # Launch exploit
    run_exploit(ip, ports_services)

    print("[✅] Adaptive strike complete.")
