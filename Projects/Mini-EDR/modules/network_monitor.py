import psutil
import time
import logging
import os
import socket
import subprocess

# Setup logging
log_file = os.path.join(os.path.dirname(__file__), '../logs/network_monitor.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')


def get_geoip_country(ip):
    try:
        result = subprocess.run(
            ['geoiplookup', ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout.strip()

        if "not found" in output.lower():
            return "Unknown"

        # Example: "GeoIP Country Edition: US, United States"
        if ", " in output:
            return output.split(", ", 1)[1]

        return "Unknown"

    except Exception:
        return "Unknown"


def monitor_connections():
    seen_connections = set()

    while True:
        # Collect IPv4 + IPv6
        all_conns = psutil.net_connections(kind='inet') + psutil.net_connections(kind='inet6')

        for conn in all_conns:
            if conn.raddr and conn.pid:  # Only outbound connections
                try:
                    ip = conn.raddr.ip
                    port = conn.raddr.port
                except:
                    continue

                key = (conn.pid, ip, port)

                if key not in seen_connections:
                    seen_connections.add(key)
                    try:
                        proc = psutil.Process(conn.pid)
                        proc_name = proc.name()

                        # GEOIP lookup
                        country = get_geoip_country(ip)

                        # Logging
                        log_message = f"Process {proc_name} (PID {conn.pid}) connected to {ip}:{port} ({country})"
                        logging.info(log_message)

                        # Console output
                        print(f"[NET ALERT] {proc_name} → {ip}:{port} ({country})")

                    except Exception:
                        pass

        time.sleep(3)
