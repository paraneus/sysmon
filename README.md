# sysmon

Simple terminal-style system monitor for Linux, built with Python and Flask.
A private learning project.

## Features

- Live CPU, RAM and disk usage, refreshed every 2 seconds
- Warning when a value goes above 80%
- RAM and disk shown as used / total in GB
- JSON API at `/api/stats`

## Stack

Python 3, Flask, psutil, HTML/CSS/JavaScript, Docker

## Run locally

```bash
pip install -r requirements.txt
python3 app.py
```

Open http://localhost:8000

## Run with Docker

```bash
docker build -t sysmon .
docker run --rm -p 8000:8000 sysmon
```

Open http://localhost:8000

Note: inside a container, psutil reads the host kernel's values, so sysmon shows the CPU and RAM of the host machine, not the limits of the container.

## Ideas

- History graph
- Email alerts
- Terminal dashboard (TUI)
- systemd service
- Kubernetes deployment with Helm
