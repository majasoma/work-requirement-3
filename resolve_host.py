import socket

hostname = "example.com"
ip_address = socket.gethostbyname(hostname)

print(f"Hei! IP-adressen til {hostname} er {ip_address}")