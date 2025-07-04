import subprocess
import re

def detect_os(ip):
    try:
        output = subprocess.check_output(
            ["ping", "-c", "1", "-W", "1", ip],
            stderr=subprocess.DEVNULL,
            universal_newlines=True
        )

        ttl_match = re.search(r"ttl[=|:](\d+)", output.lower())
        if ttl_match:
            ttl = int(ttl_match.group(1))
            if ttl <= 64:
                return "Linux/Unix"
            elif ttl <= 128:
                return "Windows"
            elif ttl <= 255:
                return "Cisco/Netzwerkgerät"
        return "Unbekannt"
    except subprocess.CalledProcessError:
        return "Offline oder keine Antwort"
    except Exception:
        return "Unbekannt"
