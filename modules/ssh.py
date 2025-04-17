# modules/ssh.py
import paramiko
import socket
import time

def try_default_ssh(ip, port):
    print(f"[📦] Trying default SSH credentials on {ip}:{port}...")
    users = ['root', 'admin', 'user']
    passwords = ['toor', 'admin', '1234', 'password']

    for user in users:
        for pw in passwords:
            try:
                sock = socket.create_connection((ip, port), timeout=3)
                t = paramiko.Transport(sock)
                t.start_client(timeout=3)
                t.auth_password(user, pw)

                if t.is_authenticated():
                    print(f"[✅] SUCCESS: {user}:{pw}")
                    t.close()
                    return
                t.close()
            except paramiko.AuthenticationException:
                continue
            except Exception as e:
                print(f"[!] SSH error: {e}")
    print("[❌] No valid SSH credentials found.")

def fingerprint_ssh_banner(ip, port):
    print(f"[🧠] Grabbing SSH banner on {ip}:{port}...")
    try:
        sock = socket.create_connection((ip, port), timeout=3)
        banner = sock.recv(1024).decode()
        print(f"[🎭] SSH Banner: {banner.strip()}")
        sock.close()
    except Exception as e:
        print(f"[!] Banner grab failed: {e}")

def run(ip, port, intel):
    fingerprint_ssh_banner(ip, port)
    try_default_ssh(ip, port)
