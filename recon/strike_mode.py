# recon/strike_mode.py
from recon.scanner import scan_target
from recon.intel import full_intel
from utils.target_scorer import score_target
from exploit.auto_exploit import run_exploit

# [⚔️ STRIKE MODE] - Smart scan + scoring + exploit in one shot

def strike_mode(ip):
    print(f"[⚔️] STRIKE MODE active on {ip}")

    # Step 1: Scan for open ports and detect services
    services = scan_target(ip)
    if not services:
        print(f"[❌] No services found on {ip}. Skipping.")
        return

    # Step 2: Intelligence gathering
    intel = full_intel(ip)
    print(f"[🧠] INTEL: {intel}")

    # Step 3: Score the target
    score = score_target(ip, services)
    print(f"[📊] Target Score: {score}")

    # Step 4: Launch exploit chain
    run_exploit(ip, services)

    print(f"[✅] STRIKE MODE completed for {ip}")
