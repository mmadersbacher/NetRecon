import socket
from scanner.constants import default_ports

def scan_ports(ip, ports=default_ports, timeout=1):
    results = []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))

            if result == 0:
                banner = ""
                try:
                    sock.sendall(b"\n")
                    banner = sock.recv(1024).decode(errors="ignore").strip()
                except:
                    pass

                ttl = get_ttl(sock)
                results.append({
                    "port": port,
                    "status": "offen",
                    "banner": banner,
                    "ttl": ttl
                })
            sock.close()
        except:
            continue

    return results

def get_ttl(sock):
    try:
        return sock.getsockopt(socket.IPPROTO_IP, socket.IP_TTL)
    except:
        return None
