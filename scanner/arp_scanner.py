from scapy.all import ARP, Ether, srp
import ipaddress

def arp_scan(subnet):
    """
    Führt einen ARP-Scan im angegebenen Subnetz durch.
    Gibt eine Liste aktiver Hosts zurück mit IP und MAC-Adresse.
    """
    try:
        ip_range = str(ipaddress.IPv4Network(subnet, strict=False))
    except Exception:
        print("[!] Ungültiges Subnetz.")
        return []

    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    answered, _ = srp(packet, timeout=2, verbose=0)

    hosts = []
    for _, received in answered:
        hosts.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return hosts
