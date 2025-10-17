import socket

def domain_to_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} → {ip}")
    except Exception as e:
        print(f"Error: {e}")
