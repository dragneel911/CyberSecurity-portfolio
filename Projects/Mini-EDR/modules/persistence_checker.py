import os
import logging
import subprocess

# Logging setup
log_file = os.path.join(os.path.dirname(__file__), '../logs/persistence_checker.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def check_startup_files():
    suspicious_files = []

    startup_paths = [
        '/etc/rc.local',
        os.path.expanduser('~/.bashrc'),
        os.path.expanduser('~/.profile'),
        '/etc/systemd/system/',
        '/etc/init.d/',
        '/etc/cron.d/',
        '/var/spool/cron/crontabs/',
    ]

    for path in startup_paths:
        if os.path.isfile(path):
            with open(path, 'r', errors='ignore') as f:
                content = f.read()
                if 'wget' in content or 'curl' in content or 'nc' in content:
                    suspicious_files.append(path)
        elif os.path.isdir(path):
            for fname in os.listdir(path):
                fpath = os.path.join(path, fname)
                if os.path.isfile(fpath):
                    with open(fpath, 'r', errors='ignore') as f:
                        content = f.read()
                        if 'wget' in content or 'curl' in content or 'nc' in content:
                            suspicious_files.append(fpath)

    for f in suspicious_files:
        logging.info(f"[PERSISTENCE ALERT] Suspicious entry found in: {f}")
        print(f"[PERSISTENCE ALERT] Suspicious entry found in: {f}")

def check_crontab():
    try:
        result = subprocess.run(['crontab', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stdout:
            lines = result.stdout.splitlines()
            for line in lines:
                if 'wget' in line or 'curl' in line or 'nc' in line:
                    logging.info("[PERSISTENCE ALERT] Suspicious crontab entry: " + line)
                    print("[PERSISTENCE ALERT] Suspicious crontab entry: " + line)
    except Exception:
        pass

def run_persistence_checks():
    check_startup_files()
    check_crontab()
