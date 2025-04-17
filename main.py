# ================= main.py =================
import argparse
from tabulate import tabulate

from exploit.auto_exploit import run_exploit
from utils.threading import threaded_runner
from utils.banner import print_banner
from recon.strike_unchained import strike_unchained
from recon.strike_mode import strike_mode
from recon.dns_tricks import run as dns_scan  # [📡 DNS]
from recon.scanner import scan_target  # [🧠 Moved to scanner.py]
from recon import adaptive_ai  # ⚠️ Import module not function to avoid circular import
from utils.target_scorer import score_target
import config

# =================== LOGIC ===================

def load_targets(file_path="targets.txt"):
    with open(file_path, "r") as f:
        targets = [line.strip() for line in f if line.strip()]
    return targets

def process_target(ip):
    ports_services = scan_target(ip)
    score = score_target(ip, ports_services)
    print(f"[+] Target Score: {score} -> {ip}")
    run_exploit(ip, ports_services)

def main():
    print_banner()
    parser = argparse.ArgumentParser()
    parser.add_argument("--strike", action="store_true", help="Run strike mode")
    parser.add_argument("--strike-unchained", action="store_true", help="Run strike unchained mode")
    parser.add_argument("--adaptive-ai", action="store_true", help="Run adaptive AI strike mode")
    parser.add_argument("--stealth", action="store_true", help="Enable stealth scan mode")
    parser.add_argument("--dns", type=str, help="Run DNS attack module against domain or IP")  # [NEW]
    args = parser.parse_args()

    if args.dns:
        print(f"[📡 DNS] Running DNS tricks against {args.dns}...")
        dns_scan(args.dns)
        return

    targets = load_targets()
    print(f"[+] Loaded {len(targets)} target(s).")

    for target in targets:
        if args.strike:
            print(f"[⚔️  STRIKE] Running Strike Mode on {target}...")
            strike_mode(target)

        elif args.strike_unchained:
            print(f"[🧨 UNCHAINED] Running Strike Unchained Mode on {target}...")
            strike_unchained(target)

        elif args.adaptive_ai:
            print(f"[🤖 AI] Running Adaptive AI Strike Mode on {target}...")
            adaptive_ai.adaptive_ai_strike(target)

        else:
            print(f"[🔍⚙️] Running Normal Recon + Exploit Mode on {target}...")
            threaded_runner(targets, worker_func=process_target, max_threads=config.MAX_THREADS)
            break

if __name__ == "__main__":
    main()
