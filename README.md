# NetRecon – Professionelles Netzwerk-Recon-Too

## Projektübersicht

NetRecon ist ein Python-basiertes Netzwerk-Scanning- und Reconnaissance-Tool, das eigenständig das lokale IP-Subnetz erkennt und aktiv nach Geräten scannt.  
Es liefert detaillierte Informationen über Hosts, offene Ports, Betriebssysteme und Hersteller. Optional kann ein anderes Subnetz angegeben werden, um gezielt zu scannen.  
Die Ergebnisse werden in einem übersichtlichen, interaktiven HTML-Report visualisiert – inklusive Portstatistiken (Chart.js) und dynamischem Netzwerkgraph (D3.js).

---

## Funktionen

- **Automatische Subnetzerkennung**: Ermittelt das lokale IPv4-Subnetz und scannt dieses eigenständig.  
- **Manuelle Subnetzeingabe**: Optional kann ein beliebiges Subnetz (z.B. `192.168.1.0/24`) als Scanziel angegeben werden.  
- **ARP-Scan** zur Erkennung aktiver Geräte im Ziel-Subnetz  
- **Port-Scan** mit Banner-Grabbing für frei wählbare Ports  
- **Betriebssystem-Erkennung** anhand von TTL-Analyse  
- **Herstellerbestimmung** via OUI Lookup der MAC-Adresse  
- **Interaktiver HTML-Report** mit:  
  - Portverteilung als Balkendiagramm  
  - Netzwerkgraph mit Hervorhebung von Gerätetypen  
  - Detaillierter Gerätetabelle mit IP, MAC, Vendor und offenen Ports

---

## Installation

1. Repository klonen:  
   ```bash
   git clone https://github.com/mmadersbacher/NetRecon.git
   cd NetRecon

    Virtuelle Umgebung erstellen und aktivieren (empfohlen):

python3 -m venv .venv
source .venv/bin/activate

Abhängigkeiten installieren:

    pip install -r requirements.txt

Nutzung

sudo python netrecon.py [--subnet <SUBNET>] [--ports <PORTS>]

    --subnet: Optionales Ziel-Subnetz für den Scan, z.B. 192.168.1.0/24. Wird kein Subnetz angegeben, erkennt NetRecon automatisch das lokale Subnetz und scannt dieses.

    --ports: Kommagetrennte Liste von Ports, z.B. 22,80,443. Standardports werden verwendet, wenn keine Angabe erfolgt.

Ergebnisse werden im Ordner output/scan_<TIMESTAMP> gespeichert, inklusive eines interaktiven HTML-Reports.
Architektur & Technologien

    Python 3 mit scapy für Low-Level Netzwerkpakete

    Frontend-Visualisierung:

        Chart.js für Balkendiagramme

        D3.js für dynamische Netzwerkgraphen

    Modulare Architektur mit klar getrennten Komponenten für Scanning, Analyse und Reporting

    Responsive, moderne HTML-Reports mit CSS Styling

Sicherheitshinweise

    Für ARP-Scan und Port-Scan sind Root- oder Administratorrechte erforderlich.

    NetRecon ist ausschließlich für den Einsatz in eigenen oder autorisierten Netzwerken vorgesehen. Unerlaubte Scans sind illegal und strafbar.

    Das Tool dient der Netzwerküberwachung, Sicherheitsanalyse und dem IT-Management – kein Angriffswerkzeug.

Weiterentwicklung

    Verbesserte OS-Erkennung (Fingerprinting)

    Automatische Klassifizierung und Icon-Integration für Gerätetypen

    Zusätzliche Exportformate (CSV, JSON)

    Erweiterte Fehlerbehandlung und Protokollierung

    Integration in professionelle Pentesting-Frameworks

