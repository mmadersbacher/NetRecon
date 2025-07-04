import argparse
import os
import json
import datetime
import subprocess

from scanner.network import scan_network
from reporting.html_report import generate_html_report
from scanner.constants import default_ports

def detect_subnet():
    try:
        result = subprocess.check_output(["ip", "-4", "addr"], universal_newlines=True)
        for line in result.splitlines():
            line = line.strip()
            if line.startswith("inet") and not line.startswith("inet 127."):
                parts = line.split()
                ip_cidr = parts[1]  # z. B. "192.168.8.101/24"
                subnet = ip_cidr.rsplit('.', 1)[0] + ".0/24"
                return subnet
    except Exception as e:
        print(f"[!] Subnet konnte nicht automatisch erkannt werden: {e}")
    return "192.168.0.0/24"

def main():

    parser = argparse.ArgumentParser(description="Netzwerk-Recon-Tool")
    parser.add_argument("--ports", type=str, help="Kommagetrennte Portliste z. B. 22,80,443")
    parser.add_argument("--subnet", type=str, help="Subnetz z. B. 192.168.8.0/24")
    args = parser.parse_args()

    if args.ports:
        try:
            ports = [int(p.strip()) for p in args.ports.split(",")]
        except:
            print("[!] Ungültiges Port-Format – fallback auf default_ports")
            ports = default_ports
    else:
        ports = default_ports

    subnet = args.subnet if args.subnet else detect_subnet()
    print(f"[+] Starte ARP-Scan auf {subnet} ...")

    results = scan_network(subnet=subnet, ports=ports)
    print(f"[✓] ARP-Scan abgeschlossen. {len(results)} Geräte gefunden.")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = os.path.join("output", f"scan_{timestamp}")
    os.makedirs(output_dir, exist_ok=True)

    raw_path = os.path.join(output_dir, "raw.json")
    with open(raw_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"[✓] Ergebnisse gespeichert unter: {raw_path}")

    generate_html_report(raw_path, output_dir)
    print(f"[✓] HTML-Report gespeichert unter: {os.path.join(output_dir, 'report.html')}")

# WICHTIG: Nur EINZIG hier darf main() aufgerufen werden!
if __name__ == "__main__":
    main()
