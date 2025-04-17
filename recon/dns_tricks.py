# recon/dns_tricks.py
import dns.resolver
import dns.query
import dns.zone
import socket

def zone_transfer(ip, domain):
    print(f"[📡] Attempting zone transfer on {domain} via {ip}...")
    try:
        z = dns.zone.from_xfr(dns.query.xfr(ip, domain, timeout=5))
        names = z.nodes.keys()
        print("[✅] Zone Transfer Succeeded! Records:")
        for n in names:
            print(f"  - {n}.{domain}")
    except Exception as e:
        print(f"[❌] Zone transfer failed: {e}")

def mdns_probe():
    print("[🔎] Probing mDNS for local services...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.settimeout(3)
        msg = b'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x09_services\x07_dns-sd\x04_udp\x05local\x00\x00\x0c\x00\x01'
        s.sendto(msg, ("224.0.0.251", 5353))
        resp, _ = s.recvfrom(1024)
        print("[✅] mDNS Response Received! Partial dump:")
        print(resp[:100])
    except Exception as e:
        print(f"[❌] mDNS probe failed: {e}")

def brute_subdomains(domain):
    print(f"[🧨] Starting subdomain brute-force on {domain}...")
    common = ['admin', 'test', 'dev', 'vpn', 'mail', 'portal', 'api', 'internal', 'login']
    for sub in common:
        fqdn = f"{sub}.{domain}"
        try:
            socket.gethostbyname(fqdn)
            print(f"[+] Found subdomain: {fqdn}")
        except:
            pass

def dns_rebind(domain):
    print(f"[🎭] Simulating DNS rebinding payload to {domain}...")
    print("[⚠️] NOTE: Full DNS rebinding requires controlled DNS server or JS-based client vector.")
    print("[💡] Use-case: Internal services accessible via SSRF can be poisoned to 127.0.0.1")

def run(domain_or_ip):
    if domain_or_ip.replace('.', '').isalpha():
        brute_subdomains(domain_or_ip)
        dns_rebind(domain_or_ip)
        try:
            ns = dns.resolver.resolve(domain_or_ip, 'NS')[0].to_text()
            zone_transfer(ns, domain_or_ip)
        except:
            print("[ℹ️] Failed to resolve nameserver or perform zone transfer.")
    else:
        mdns_probe()
