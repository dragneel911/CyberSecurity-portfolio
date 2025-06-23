from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import os
import time

# Logging setup
log_file = os.path.join(os.path.dirname(__file__), '../logs/file_watcher.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

WATCH_PATH = '/tmp'  # You can change this to any folder you want to monitor

class FileMonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f"Modified: {event.src_path}")
        print(f"[FILE ALERT] Modified: {event.src_path}")

    def on_created(self, event):
        logging.info(f"Created: {event.src_path}")
        print(f"[FILE ALERT] Created: {event.src_path}")

    def on_deleted(self, event):
        logging.info(f"Deleted: {event.src_path}")
        print(f"[FILE ALERT] Deleted: {event.src_path}")

def watch_files():
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_PATH, recursive=True)
    observer.start()
    print(f"[INFO] Watching {WATCH_PATH} for file changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
