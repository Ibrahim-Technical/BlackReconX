# modules/mysql.py
import pymysql

def try_default_credentials(ip, port):
    print(f"[📦] Attempting MySQL login on {ip}:{port} with default creds...")
    default_users = ["root", "admin", "test"]
    default_passwords = ["", "root", "admin", "1234", "password"]

    for user in default_users:
        for pw in default_passwords:
            try:
                conn = pymysql.connect(host=ip, port=port, user=user, password=pw, connect_timeout=3)
                print(f"[✅] SUCCESS: {user}:{pw}")
                with conn.cursor() as cursor:
                    cursor.execute("SHOW DATABASES;")
                    dbs = cursor.fetchall()
                    print("[📚] Databases:", [db[0] for db in dbs])
                conn.close()
                return
            except pymysql.err.OperationalError:
                continue
            except Exception as e:
                print(f"[!] Error: {e}")
    print("[❌] No valid credentials found.")

def run(ip, port, intel):
    try_default_credentials(ip, port)
