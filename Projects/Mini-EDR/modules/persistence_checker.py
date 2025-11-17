import os
import logging
import subprocess

# Logging setup
log_file = os.path.join(os.path.dirname(__file__), '../logs/persistence_checker.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')


# ------------------------------
# Helper: detect only real malicious lines
# ------------------------------
def is_suspicious_line(line):
    line = line.strip()

    # Ignore comments
    if line.startswith("#"):
        return False

    # Patterns that usually indicate malicious persistence
    suspicious_keywords = [
        "wget ",
        "curl ",
        "nc ",
        "bash -i",
        "sh -i",
        "python -c",
        "base64 -d",
        "| sh",
        "| bash"
    ]

    # Only return True if keyword appears in an active command
    return any(keyword in line for keyword in suspicious_keywords)


# ------------------------------
# Scan all startup/persistence locations
# ------------------------------
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
            if scan_file(path):
                suspicious_files.append(path)

        elif os.path.isdir(path):
            for fname in os.listdir(path):
                fpath = os.path.join(path, fname)
                if os.path.isfile(fpath):
                    if scan_file(fpath):
                        suspicious_files.append(fpath)

    for f in suspicious_files:
        logging.info(f"[PERSISTENCE ALERT] Suspicious entry found in: {f}")
        print(f"[PERSISTENCE ALERT] Suspicious entry found in: {f}")


# ------------------------------
# Scan a single file safely
# ------------------------------
def scan_file(filepath):
    try:
        with open(filepath, 'r', errors='ignore') as f:
            for line in f:
                if is_suspicious_line(line):
                    return True
    except:
        pass
    return False


# ------------------------------
# Check user crontab entries
# ------------------------------
def check_crontab():
    try:
        result = subprocess.run(['crontab', '-l'], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)

        if result.stdout:
            for line in result.stdout.splitlines():
                if is_suspicious_line(line):
                    logging.info("[PERSISTENCE ALERT] Suspicious crontab entry: " + line)
                    print("[PERSISTENCE ALERT] Suspicious crontab entry: " + line)

    except Exception:
        pass


# ------------------------------
# Main runner
# ------------------------------
def run_persistence_checks():
    check_startup_files()
    check_crontab()
