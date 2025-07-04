def build_graph_data(data):
    nodes = []
    links = []

    router_ip = None
    # Suche ersten Router (z.B. mit IP 192.168.x.1) oder nimm erstes Gerät als Router
    for device in data:
        ip = device["ip"]
        if ip.endswith(".1"):
            router_ip = ip
            break
    if not router_ip and data:
        router_ip = data[0]["ip"]

    nodes.append({"id": router_ip, "label": f"Router\n{router_ip}", "type": "router"})

    for device in data:
        ip = device["ip"]
        if ip == router_ip:
            continue
        nodes.append({"id": ip, "label": f"{ip}\n{device['vendor']}", "type": "client"})
        links.append({"source": router_ip, "target": ip})

    return {"nodes": nodes, "links": links}

def build_port_statistics(data):
    port_counts = {}
    for device in data:
        for port in device["ports"]:
            p = port["port"]
            port_counts[p] = port_counts.get(p, 0) + 1
    return port_counts
