import json
import os
import shutil
from reporting.visualizer import build_graph_data, build_port_statistics

TEMPLATE_PATH = "templates/report_template.html"
STATIC_SOURCE = "static"
OUTPUT_FILENAME = "report.html"

def generate_html_report(json_path, output_dir):
    with open(json_path, "r") as f:
        data = json.load(f)

    graph_data = build_graph_data(data)
    port_stats = build_port_statistics(data)

    with open(TEMPLATE_PATH, "r") as f:
        html = f.read()

    html = html.replace("<!--GRAPH_DATA-->", json.dumps(graph_data))
    html = html.replace("<!--PORT_STATS-->", json.dumps(port_stats))
    html = html.replace("<!--RAW_TABLE-->", generate_html_table(data))

    output_path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(output_path, "w") as f:
        f.write(html)

    static_target = os.path.join(output_dir, "static")
    if not os.path.exists(static_target):
        shutil.copytree(STATIC_SOURCE, static_target)

def generate_html_table(results):
    html = "<table><thead><tr><th>IP</th><th>MAC</th><th>Vendor</th><th>Ports</th></tr></thead><tbody>"

    for device in results:
        ports = "<br>".join([f"{p['port']} → {p['banner']}" for p in device['ports']])
        html += f"<tr><td>{device['ip']}</td><td>{device['mac']}</td><td>{device['vendor']}</td><td>{ports}</td></tr>"

    html += "</tbody></table>"
    return html
