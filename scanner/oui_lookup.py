def load_oui_data(filepath="data/oui.txt"):
    oui_dict = {}
    try:
        with open(filepath, "r") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) == 2:
                    oui, vendor = parts
                    oui_dict[oui.upper()] = vendor
    except FileNotFoundError:
        pass
    return oui_dict

OUI_DATA = load_oui_data()

def get_vendor(mac_address):
    oui = mac_address.upper().replace(":", "")[:6]
    return OUI_DATA.get(oui, "Unbekannt")
