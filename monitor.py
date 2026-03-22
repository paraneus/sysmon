import psutil

def get_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "cpu": {
            "percent": cpu,
            "warning": cpu > 80
        },
        "ram": {
            "percent": ram.percent,
            "used_gb": round(ram.used / (1024**3), 1),
            "total_gb": round(ram.total / (1024**3), 1),
            "warning": ram.percent > 80
        },
        "disk": {
            "percent": disk.percent,
            "used_gb": round(disk.used / (1024**3), 1),
            "total_gb": round(disk.total / (1024**3), 1),
            "warning": disk.percent > 80
        }
    }