# recon/scanner.py
import subprocess
import random
import time
import nmap
from tabulate import tabulate
import config


def smart_sleep():
    time.sleep(random.uniform(0.2, 1.5))

def stealth_flag():
    return f"--source-port={random.randint(1024, 65535)} --ttl={random.choice([64, 128, 255])}"

def smart_analysis(reason, state):
    if state == "open":
        return "✅ Open"
    elif state == "closed":
        return "❌ Closed"
    elif state == "filtered":
        if "no-response" in reason.lower():
            return "⛔ Filtered (No Response)"
        elif "firewall" in reason.lower():
            return "🛡 Blocked by Firewall"
        else:
            return "🔒 Possibly Hidden/Protected"
    else:
        return "❓ Unknown"

def run_masscan(ip, ports=config.TCP_PORTS, stealth=False):
    print(f"[⚙️] Running masscan on {ip} ports {ports}...")
    flags = stealth_flag() if stealth else ""
    try:
        result = subprocess.check_output(f"masscan {ip} -p{ports} --rate={config.MASSCAN_RATE} {flags}", shell=True, stderr=subprocess.DEVNULL).decode()
        open_ports = [int(line.split()[-1]) for line in result.splitlines() if "open tcp" in line]
        return open_ports
    except Exception as e:
        print(f"[!] Masscan error: {e}")
        return []

def run_nmap_service_scan(ip, ports):
    ports_str = ",".join(str(p) for p in ports)
    print(f"[🔎] Running nmap service detection on {ip}:{ports_str} ...")
    scanner = nmap.PortScanner()
    scanner.scan(ip, ports_str, arguments="-sV")

    results_table = []
    detected = {}

    for p in ports:
        try:
            name = scanner[ip]['tcp'][p]['name']
            state = scanner[ip]['tcp'][p]['state']
            reason = scanner[ip]['tcp'][p]['reason']
            analysis = smart_analysis(reason, state)
            results_table.append([p, 'tcp', state, name, reason, analysis])
            detected[p] = name
        except:
            results_table.append([p, 'tcp', 'unknown', 'unknown', 'N/A', '❓ Unknown'])
            detected[p] = 'unknown'

    print("\n[📋] Service Detection Result:")
    print(tabulate(results_table, headers=["Port", "Protocol", "State", "Service", "Reason", "Insight"], tablefmt="fancy_grid"))
    return detected

def scan_target(ip, stealth=False):
    open_ports = run_masscan(ip, stealth=stealth)
    if not open_ports:
        print(f"[!] No open ports found on {ip}.")
        return {}
    return run_nmap_service_scan(ip, open_ports)
