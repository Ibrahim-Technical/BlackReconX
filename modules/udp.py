
import socket
from config import TIMEOUT

def exploit_udp(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(TIMEOUT)
        s.sendto(b"Hello", (ip, port))
        res, _ = s.recvfrom(1024)
        print(f"[UDP {port}] 🧾 Response: {res.decode(errors='ignore')}")
    except socket.timeout:
        print(f"[UDP {port}] ❌ No response (timeout)")
    except Exception as e:
        print(f"[UDP {port}] ❌ Error: {e}")
    finally:
        s.close()
