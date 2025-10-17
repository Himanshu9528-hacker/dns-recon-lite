import socket

def ip_to_domain(ip):
    try:
        domain = socket.gethostbyaddr(ip)
        print(f"{ip} → {domain[0]}")
    except Exception as e:
        print(f"Error: {e}")
