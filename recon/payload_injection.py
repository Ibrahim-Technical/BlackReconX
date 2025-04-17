import random
import time
import socket

def inject_payload(ip, latency, os_guess):
    print(f"\n[PAYLOAD] 🚀 Adaptive Payload Injection for {ip}")
    print(f"[PAYLOAD] OS Guess: {os_guess} | Latency: {latency:.3f}s")

    # Define behavior based on OS & timing
    if os_guess == "Linux" and latency < 0.3:
        print(f"[PAYLOAD] 🧪 Injecting Linux web probes on {ip}:80")
        simulate_http_payload(ip)

    elif os_guess == "Windows" and latency < 0.3:
        print(f"[PAYLOAD] 🔍 Attempting VNC fuzz on {ip}:5900")
        simulate_vnc_payload(ip)

    elif latency > 1.5:
        print(f"[PAYLOAD] 😴 Target seems idle or filtered — skipping aggressive payloads.")

    else:
        print(f"[PAYLOAD] 🤔 No strong fingerprint — injecting generic recon payload.")
        simulate_generic_payload(ip)


# ===========================
# PAYLOAD SIMULATION LOGIC
# ===========================

def simulate_http_payload(ip):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, 80))
        sock.send(b"GET /?test=ai_probe HTTP/1.1\r\nHost: %s\r\n\r\n" % ip.encode())
        res = sock.recv(512)
        print(f"[HTTP PAYLOAD] ✅ Response: {res[:60].decode(errors='ignore')}...")
        sock.close()
    except Exception as e:
        print(f"[HTTP PAYLOAD] ❌ Error: {e}")


def simulate_vnc_payload(ip):
    try:
        sock = socket.socket()
        sock.settimeout(3)
        sock.connect((ip, 5900))
        sock.send(b"RFB 003.003\n")
        res = sock.recv(64)
        print(f"[VNC PAYLOAD] ✅ VNC Response: {res}")
        sock.close()
    except Exception as e:
        print(f"[VNC PAYLOAD] ❌ Error: {e}")


def simulate_generic_payload(ip):
    ports = [21, 23, 80, 443]
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1.5)
            sock.connect((ip, port))
            sock.send(b"PING\n")
            res = sock.recv(64)
            print(f"[GENERIC PAYLOAD] ✅ Port {port}: Response = {res[:40].decode(errors='ignore')}")
            sock.close()
        except:
            print(f"[GENERIC PAYLOAD] ⚠️ Port {port} - No response")
