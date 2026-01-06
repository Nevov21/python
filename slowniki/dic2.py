processes = {
    "nginx": "running",
    "mysql": "stopped",
    "apache": "running",
}

for proc, status in processes.items():
    if status != "running":
        print(f"ALERT! {proc} jest {status}")