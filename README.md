# sysmon

Simple terminal-style system monitor for Linux, built with Python and Flask.
A private learning project.

## Features

- Live CPU, RAM and disk usage, refreshed every 2 seconds
- Warning when a value goes above 80%
- RAM and disk shown as used / total in GB
- JSON API at `/api/stats`

## Stack

Python 3, Flask, psutil, HTML/CSS/JavaScript

## Run

```bash
pip install flask psutil
python3 app.py
```

Open http://localhost:8000

## Ideas

- History graph
- Email alerts
- Terminal dashboard (TUI)
- systemd service
