from collections import defaultdict
from datetime import datetime
import csv
import os

ip_counter = defaultdict(int)

ALERT_FILE = "alerts.csv"

if not os.path.exists(ALERT_FILE):
    with open(ALERT_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Source IP", "Threat Type", "Severity"])


def detect_threat(packet):
    alerts = []

    if packet.haslayer("IP"):
        src_ip = packet["IP"].src

        ip_counter[src_ip] += 1

        # Port Scan Detection
        if packet.haslayer("TCP"):
            if ip_counter[src_ip] > 20:
                alerts.append({
                    "ip": src_ip,
                    "type": "Possible Port Scanning",
                    "severity": "High"
                })

        # Ping Flood Detection
        if packet.haslayer("ICMP"):
            if ip_counter[src_ip] > 10:
                alerts.append({
                    "ip": src_ip,
                    "type": "Ping Flood Attack",
                    "severity": "Medium"
                })

    for alert in alerts:
        save_alert(alert)

    return alerts


def save_alert(alert):
    with open(ALERT_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            alert["ip"],
            alert["type"],
            alert["severity"]
        ])