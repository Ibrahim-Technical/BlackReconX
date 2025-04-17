# recon/intel.py
import requests
import socket
import re

# =================== WAF DETECTION ===================

def detect_waf(ip):
    waf_signatures = {
        'cloudflare': ['cloudflare', '__cfduid', '__cf_bm'],
        'sucuri': ['sucuri'],
        'akamai': ['akamai'],
        'imperva': ['imperva'],
        'barracuda': ['barra'],
    }
    try:
        res = requests.get(f"http://{ip}", timeout=3)
        headers = str(res.headers).lower()
        body = res.text.lower()

        for waf, signs in waf_signatures.items():
            if any(sig in headers or sig in body for sig in signs):
                return waf.capitalize()
    except:
        return "Unknown"
    return "None"

# =================== CMS DETECTION ===================

def detect_cms(ip):
    cms_patterns = {
        'wordpress': ['/wp-login.php', '/wp-admin', 'wp-content'],
        'joomla': ['/administrator', 'joomla'],
        'drupal': ['/user/login', 'drupal'],
        'ghost': ['/ghost/', 'ghost'],
    }
    try:
        res = requests.get(f"http://{ip}", timeout=3)
        html = res.text.lower()

        for cms, patterns in cms_patterns.items():
            if any(p in html for p in patterns):
                return cms.capitalize()
    except:
        return "Unknown"
    return "None"

# =================== CLOUD INFRA DETECTION ===================

def detect_cloud(ip):
    try:
        domain = socket.gethostbyaddr(ip)[0]
        if any(x in domain for x in ['amazonaws.com', 'cloudapp.azure.com', 'googleusercontent.com']):
            if 'amazon' in domain:
                return "AWS"
            elif 'azure' in domain:
                return "Azure"
            elif 'google' in domain:
                return "GCP"
    except:
        return "Unknown"
    return "None"

# =================== AGGREGATOR ===================

def full_intel(ip):
    return {
        'WAF': detect_waf(ip),
        'CMS': detect_cms(ip),
        'Cloud': detect_cloud(ip)
    }
