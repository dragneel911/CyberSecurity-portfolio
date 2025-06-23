import psutil
import time
import logging
import os

# Setup logging
log_file = os.path.join(os.path.dirname(__file__), '../logs/process_monitor.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def monitor_processes():
    known_procs = set(p.pid for p in psutil.process_iter())
    while True:
        current_procs = {p.pid: p.info for p in psutil.process_iter(['pid', 'name', 'exe', 'username'])}
        new_pids = set(current_procs.keys()) - known_procs

        for pid in new_pids:
            proc = current_procs[pid]
            logging.info(f"New process detected: PID={pid}, Name={proc['name']}, Path={proc['exe']}, User={proc['username']}")
            print(f"[ALERT] New process: {proc['name']} (PID {pid})")

        known_procs = set(current_procs.keys())
        time.sleep(3)
