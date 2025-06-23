import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging

log_file = "logs/file_watcher.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

WATCH_PATH = "/tmp"  # or any path you want to monitor

def log_event(event_type, path):
    message = f"[FILE ALERT] {event_type}: {path}"
    print(message)
    logging.info(message)

class FileWatcherHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            if filename.startswith('#') or filename.startswith('.'):
                return
            log_event("Modified", event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            log_event("Created", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            log_event("Deleted", event.src_path)

def watch_files():
    event_handler = FileWatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
