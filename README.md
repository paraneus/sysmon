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

## Run on Kubernetes (GitOps)

Manifests are in `deploy/` (Deployment + Service).
I deploy them with [Argo CD](https://argo-cd.readthedocs.io/) on a local k3d cluster:

```bash
docker build -t sysmon:0.1 .
k3d image import sysmon:0.1 -c lab
```

Argo CD watches this repo (path `deploy/`) and syncs the manifests into the cluster.

To open it locally:

```bash
kubectl port-forward svc/sysmon-ui 8000:8000
```

Open http://localhost:8000

## Ideas

- History graph
- Email alerts
- Terminal dashboard (TUI)
- systemd service
- Kubernetes deployment with Helm
- CI pipeline that builds and pushes the image
- Resource requests and limits
