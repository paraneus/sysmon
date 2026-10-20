# sysmon

Simple terminal-style system monitor for Linux, built with Python and Flask.
A private learning project.

## Features

- Live CPU, RAM and disk usage, refreshed every 2 seconds
- Warning when a value goes above 80%
- RAM and disk shown as used / total in GB
- JSON API at `/api/stats`

## Stack

Python 3, Flask, psutil, HTML/CSS/JavaScript, Docker, Kubernetes (k3d), Argo CD

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

Everything needed to run sysmon on a local k3d cluster lives in this repo:

| Folder | What it describes |
|---|---|
| `cluster/` | the k3d cluster itself (ports bound to 127.0.0.1 only) |
| `deploy/` | Kubernetes manifests (Deployment + NodePort Service) |
| `argocd/` | the Argo CD application that syncs `deploy/` |

### Quick start (plain kubectl)

```bash
k3d cluster create --config cluster/k3d-lab.yaml
docker build -t sysmon:0.1 .
k3d image import sysmon:0.1 -c lab
kubectl apply -f deploy/
```

Open http://localhost:30080

### GitOps way (Argo CD)

Instead of `kubectl apply -f deploy/`, install
[Argo CD](https://argo-cd.readthedocs.io/) and let it sync this repo
(after creating the cluster and importing the image as above):

```bash
kubectl create namespace argocd
kubectl apply -n argocd --server-side -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl apply -f argocd/sysmon.yaml
```

Argo CD watches `deploy/` in this repo and keeps the cluster in sync
with Git (auto-sync + self-heal). A change merged to `main` shows up
in the cluster without running kubectl by hand.

## Ideas

- History graph
- Email alerts
- Terminal dashboard (TUI)
- systemd service
- Kubernetes deployment with Helm
- CI pipeline that builds and pushes the image
- Resource requests and limits
