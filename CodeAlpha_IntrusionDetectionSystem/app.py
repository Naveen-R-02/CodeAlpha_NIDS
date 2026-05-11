from flask import Flask, render_template
from flask_socketio import SocketIO
from scapy.all import sniff
from detector import detect_threat
import threading

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

stats = {
    "total_packets": 0,
    "threats": 0,
    "high": 0,
    "medium": 0
}


@app.route("/")
def index():
    return render_template("index.html")


def process_packet(packet):

    stats["total_packets"] += 1

    alerts = detect_threat(packet)

    if alerts:

        stats["threats"] += len(alerts)

        for alert in alerts:

            if alert["severity"] == "High":
                stats["high"] += 1

            if alert["severity"] == "Medium":
                stats["medium"] += 1

            socketio.emit("alert", {
                "ip": alert["ip"],
                "type": alert["type"],
                "severity": alert["severity"],
                "total_packets": stats["total_packets"],
                "threats": stats["threats"],
                "high": stats["high"],
                "medium": stats["medium"]
            })


def start_sniffing():
    sniff(prn=process_packet, store=False, iface="Software Loopback Interface 1")
    


if __name__ == "__main__":

    thread = threading.Thread(target=start_sniffing)
    thread.daemon = True
    thread.start()

    socketio.run(app, debug=True)