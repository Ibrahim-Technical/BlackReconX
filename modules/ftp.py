# modules/ftp.py
from ftplib import FTP, error_perm

def try_anonymous_login(ip, port):
    print(f"[📦] Attempting anonymous FTP login on {ip}:{port}...")
    try:
        ftp = FTP()
        ftp.connect(ip, port, timeout=3)
        ftp.login()
        print("[✅] Anonymous login successful.")
        files = ftp.nlst()
        print("[📁] Directory listing:", files)
        ftp.quit()
    except error_perm as e:
        print(f"[❌] Anonymous login denied: {e}")
    except Exception as e:
        print(f"[!] FTP error: {e}")

def try_file_upload(ip, port):
    print(f"[📦] Attempting file upload to FTP on {ip}:{port}...")
    try:
        ftp = FTP()
        ftp.connect(ip, port, timeout=3)
        ftp.login()
        with open("payload.txt", "w") as f:
            f.write("This is a test payload.\n")
        with open("payload.txt", "rb") as f:
            ftp.storbinary("STOR payload.txt", f)
        print("[✅] File uploaded successfully.")
        ftp.quit()
    except Exception as e:
        print(f"[❌] Upload failed: {e}")

def run(ip, port, intel):
    try_anonymous_login(ip, port)
    try_file_upload(ip, port)  # Run regardless — login will fail silently if not anonymous
