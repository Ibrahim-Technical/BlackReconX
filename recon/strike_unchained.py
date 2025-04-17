import socket
import random
from scapy.all import IP, TCP, sr1, RandShort, ICMP, sr
import time

def strike_unchained(ip):
    print(f"\n🔥 STRIKE UNCHAINED MODE LAUNCHED AGAINST {ip}")

    stealth_ports = [22, 80, 443, 445, 8080, 31337, 5900]
    # ------------------- [1] Stealth Scan -------------------
    print(f"[UNCHAINED] 🧬 Stealth Packet Probing on {ip}...")
    for port in stealth_ports:
        pkt = IP(dst=ip)/TCP(dport=port, flags="S", window=1024)
        resp = sr1(pkt, timeout=2, verbose=0)
        if resp:
            if resp.haslayer(TCP):
                flags = resp.getlayer(TCP).flags
                if flags == 0x12:
                    print(f"[UNCHAINED] ✅ {ip}:{port} ➜ SYN-ACK (Open?)")
                elif flags == 0x14:
                    print(f"[UNCHAINED] ❌ {ip}:{port} ➜ RST (Closed)")
                else:
                    print(f"[UNCHAINED] 🌀 {ip}:{port} ➜ TCP Flags: {flags}")
            else:
                print(f"[UNCHAINED] ❗ {ip}:{port} ➜ Unrecognized response")
        else:
            print(f"[UNCHAINED] ❌ {ip}:{port} ➜ No response")

    # ------------------- [2] Host Header Injection -------------------
    print(f"\n[UNCHAINED] 🌐 Host Header Injection + SSRF Tricks on {ip}...")
    fake_headers = {
        "Host": "admin.local",
        "X-Forwarded-For": "127.0.0.1",
        "X-Real-IP": "127.0.0.1",
    }
    for header, value in fake_headers.items():
        print(f"[UNCHAINED] 🧪 Trying header {header}: {value}")

    # ------------------- [3] DNS Rebinding Simulation -------------------
    print(f"\n[UNCHAINED] 🧠 DNS Rebinding Simulation on {ip}...")
    domains = [f"rebind-{random.randint(1000,9999)}.lan" for _ in range(3)]
    for d in domains:
        print(f"[UNCHAINED] ✅ {d} did not resolve")

    # ------------------- [4] TTL/IPID Fingerprinting -------------------
    print(f"\n[UNCHAINED] 📍 TTL/IPID Fingerprinting on {ip}...")
    pkt = IP(dst=ip)/ICMP()
    resp = sr1(pkt, timeout=2, verbose=0)
    if resp:
        ttl = resp.ttl
        ipid = resp.id
        guess = "Linux" if ttl <= 64 else "Windows" if ttl <= 128 else "Unknown"
        print(f"[UNCHAINED] 🧠 TTL={ttl} | IPID={ipid} ➜ Guess: {guess}")
    else:
        print(f"[UNCHAINED] ❌ No ICMP response")

    # ------------------- [5] ARP STORM -------------------
    print(f"\n[UNCHAINED] ⚡ ARP Storm Analysis on {ip}...")
    try:
        from scapy.all import arping
        arping(ip, timeout=2, verbose=0)
        print(f"[UNCHAINED] ✅ ARP response captured (or silent fail)")
    except:
        print(f"[UNCHAINED] ❄️ No ARP responses")

    # ------------------- [6] Protocol Fingerprints -------------------
    print(f"\n[UNCHAINED] 🧪 Protocol Fingerprints (SMB/Telnet/VNC) on {ip}...")
    test_ports = [445, 23, 5900]
    for port in test_ports:
        try:
            sock = socket.socket()
            sock.settimeout(2)
            sock.connect((ip, port))
            banner = sock.recv(1024).decode(errors="ignore")
            print(f"[UNCHAINED] ✅ {ip}:{port} ➜ {banner.strip()}")
            sock.close()
        except:
            print(f"[UNCHAINED] ❌ {ip}:{port} ➜ No response or blocked")

    # ------------------- [7] ACK PROBE -------------------
    print(f"\n[UNCHAINED] 🛰️ ACK Probe Scan on {ip}...")
    for port in stealth_ports:
        pkt = IP(dst=ip)/TCP(dport=port, flags="A")
        resp = sr1(pkt, timeout=2, verbose=0)
        if resp and resp.haslayer(TCP):
            print(f"[UNCHAINED] 🧭 {ip}:{port} ➜ TCP flags: {resp.getlayer(TCP).flags}")
        else:
            print(f"[UNCHAINED] 🕵️ {ip}:{port} ➜ No response or TCP reset")
