import psutil
import time
import logging
import os
import socket

# Setup logging
log_file = os.path.join(os.path.dirname(__file__), '../logs/network_monitor.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def monitor_connections():
    seen_connections = set()

    while True:
        for conn in psutil.net_connections(kind='inet'):
            if conn.raddr and conn.pid:
                key = (conn.pid, conn.raddr.ip, conn.raddr.port)
                if key not in seen_connections:
                    seen_connections.add(key)
                    try:
                        proc = psutil.Process(conn.pid)
                        proc_name = proc.name()
                        logging.info(f"Process {proc_name} (PID {conn.pid}) connected to {conn.raddr.ip}:{conn.raddr.port}")
                        print(f"[NET ALERT] {proc_name} → {conn.raddr.ip}:{conn.raddr.port}")
                    except Exception:
                        pass

        time.sleep(5)