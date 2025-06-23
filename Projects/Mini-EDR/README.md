# 🧠 Mini EDR – Endpoint Threat Detection System

A simple, educational Endpoint Detection and Response (EDR) project written in Python.  
It monitors processes, network activity, file system changes, and persistence techniques in real-time.

> 🔒 Built for cybersecurity learners and tinkerers!

---

## 📁 Features

| Module               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| 👀 Process Monitor    | Detects new processes running on the system                                |
| 🌐 Network Monitor    | Logs all outbound network connections made by any process                  |
| 🗂️ File Watcher       | Watches for file creation, deletion, or modification in sensitive folders  |
| 🧬 Persistence Checker| Detects potential persistence mechanisms like crontabs or startup edits    |

---

## 🧰 Requirements

- Python 3.8+
- Linux or Ubuntu VM
- Install required Python modules:

```bash
pip install psutil watchdog

📦 Project Structure
mini-edr/
│
├── main.py                      # Entry point – runs all modules
├── requirements.txt             # (Optional) Dependencies list
│
├── modules/
│   ├── process_monitor.py       # Monitors running processes
│   ├── network_monitor.py       # Tracks network connections
│   ├── file_watcher.py          # File Integrity Monitoring
│   └── persistence_checker.py   # Startup/persistence detection
│
├── logs/
│   ├── process_monitor.log
│   ├── network_monitor.log
│   ├── file_watcher.log
│   └── persistence_checker.log

Run main.py 

 Customization 📂(This is because linux and windows have different folders to watch and monitor my code is mainly for a linux environment)
To change what folders are watched:

Edit WATCH_PATH in file_watcher.py

To monitor different startup locations:

Edit the startup_paths list in persistence_checker.py
