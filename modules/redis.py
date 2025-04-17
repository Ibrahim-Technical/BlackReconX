# modules/redis.py
import socket

def test_unauth_redis(ip, port):
    print(f"[📦] Testing for unauthenticated Redis on {ip}:{port}...")
    try:
        s = socket.create_connection((ip, port), timeout=3)
        s.send(b"INFO\r\n")
        resp = s.recv(4096).decode(errors='ignore')
        if "redis_version" in resp:
            print(f"[✅] Unauthenticated Redis detected! Version info:\n{resp.splitlines()[1]}")
        else:
            print("[❌] Redis server did not respond as expected.")
        s.close()
    except Exception as e:
        print(f"[!] Redis test failed: {e}")

def try_module_load_rce(ip, port):
    print(f"[⚠️] Attempting Redis RCE via module load (mock)...")
    # This is placeholder logic. Actual RCE would involve sending crafted binary payloads.
    print("[🔬] NOTE: Full module RCE requires native payloads. PoC only.")
    # Add actual module loading here with custom payload if you have binary module ready

def run(ip, port, intel):
    test_unauth_redis(ip, port)
    try_module_load_rce(ip, port)
