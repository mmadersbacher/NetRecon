from scanner.arp_scanner import arp_scan
from scanner.banner_port_scanner import scan_ports
from scanner.os_detection import detect_os
from scanner.oui_lookup import get_vendor

def scan_network(subnet, ports):
    hosts = arp_scan(subnet)
    results = []

    for host in hosts:
        ip = host["ip"]
        mac = host["mac"]
        vendor = get_vendor(mac)
        open_ports = scan_ports(ip, ports)
        os_name = detect_os(ip) or "Unbekannt"

        results.append({
            "ip": ip,
            "mac": mac,
            "vendor": vendor,
            "ports": open_ports,
            "os": os_name,
        })

    return results
