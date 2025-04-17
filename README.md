# BlackReconX Framework

BlackReconX is an advanced offensive security framework for smart reconnaissance and multi-stage exploitation.  
It combines adaptive intelligence, modular plugins, and automated attack pipelines — designed for professionals, students, and red teamers.

## 🔥 Features

- 🎯 **Strike Mode** – Automated detection & exploitation of open ports/services  
- 🧠 **Adaptive AI Strike** – Learns from responses, selects optimized attack paths  
- 🕵️ **Strike Unchained** – Exploits stealthy systems even when ports are closed (e.g. DNS rebinding, HTTP smuggling)  
- 🔐 **Post-SSH Actions** – Automatically runs post-exploit scripts upon successful SSH login  
- 🧩 **Modular Plugin System** – Extendable architecture (FTP, SMB, SSH, HTTP...)  
- 📡 **Multi-IP Targeting** – Scan and attack multiple IPs or networks concurrently  
- 🛡️ **Evasion Techniques** – Random User-Agents, timing delays, and header spoofing  
- 🔍 **Smart Fingerprinting** – Detects CMS, WAF, web server, OS, and technologies automatically

---

## 🚀 Quick Start

```bash
git clone https://github.com/Ibrahim-Technical/BlackReconX.git
cd BlackReconX
python3 main.py --mode strike --target 192.168.1.0/24

