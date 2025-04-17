# modules/smb.py
from impacket.smbconnection import SMBConnection
import socket

def test_null_session(ip, port):
    print(f"[📦] Testing SMB null session on {ip}:{port}...")
    try:
        conn = SMBConnection(ip, ip, sess_port=port)
        conn.login('', '')  # Null session
        shares = conn.listShares()
        print("[✅] Null session succeeded! Shares:")
        for share in shares:
            print(f"  - {share['shi1_netname'][:-1]}")
        conn.close()
    except Exception as e:
        print(f"[❌] Null session failed: {e}")

def check_eternalblue_fingerprint(ip, port):
    print(f"[🧬] Checking for signs of EternalBlue vulnerability on {ip}:{port}...")
    try:
        sock = socket.create_connection((ip, port), timeout=3)
        sock.send(b"\x00\x00\x00\x85\xff\x53\x4d\x42\x72\x00\x00\x00\x00\x18\x53\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
        banner = sock.recv(1024)
        if b"Windows" in banner:
            print(f"[⚠️] SMB fingerprint suggests possible EternalBlue target (manual validation needed).")
        else:
            print("[ℹ️] SMB fingerprint inconclusive.")
        sock.close()
    except Exception as e:
        print(f"[!] Fingerprint error: {e}")

def run(ip, port, intel):
    test_null_session(ip, port)
    check_eternalblue_fingerprint(ip, port)
