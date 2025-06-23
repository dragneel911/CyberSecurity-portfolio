import threading
from modules import process_monitor, network_monitor, file_watcher, persistence_checker

if __name__ == "__main__":
    print("[*] Mini EDR started...")

    # Create threads for each module
    t1 = threading.Thread(target=process_monitor.monitor_processes, daemon=True)
    t2 = threading.Thread(target=network_monitor.monitor_connections, daemon=True)
    t3 = threading.Thread(target=file_watcher.watch_files, daemon=True)
    t4 = threading.Thread(target=persistence_checker.run_persistence_checks, daemon=True)

    # Start the threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    try:
        while True:
            pass  # Keeps the main thread alive
    except KeyboardInterrupt:
        print("\n[!] Mini EDR stopped by user.")
