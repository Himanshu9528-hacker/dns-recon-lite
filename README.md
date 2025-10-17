# 🕵️‍♂️ DNS Recon Lite

Convert domains to IPs and IPs to domains—educational DNS toolkit for awareness and recon labs.

## 🎯 Features

- 🌐 Domain to IP conversion
- 🔁 IP to domain (reverse DNS)
- 🧠 Educational use only
- 🛠 Single Python script (CLI + Flask)

---

## ⚙️ Installation

```bash
git clone https://github.com/Himanshu9528-hacker/dns-recon-lite.git
cd dns-recon-lite
pip install flask


🧪 Usage
🔹 Domain to IP
```bash
python dns_toolkit.py --domain google.com

🔹 IP to Domain
```bash
python dns_toolkit.py --ip 142.250.192.14

🔹 Run Web Interface
bash
python dns_toolkit.py --web


Then open in browser:

Lookup: http://localhost:5000/lookup?domain=google.com

Reverse: http://localhost:5000/reverse?ip=142.250.192.14

📁 Folder Structure
dns-recon-lite/
├── dns_toolkit.py
├── README.md

⚠️ Disclaimer
This tool is for educational and awareness purposes only. 
Do not use it for unauthorized scanning or real-world enumeration.

📬 Contact
Made with 🧠 by Himanshu9528-hacker
 Feel free to fork, star, or contribute!

