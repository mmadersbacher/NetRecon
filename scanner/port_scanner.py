import socket

def scan_ports(ip, ports=None, timeout=0.5):
    if ports is None:
        ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

    open_ports = []

    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                if s.connect_ex((ip, port)) == 0:
                    open_ports.append(port)
        except:
            continue

    return open_ports
