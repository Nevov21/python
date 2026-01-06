errors = []

with open("/var/log/messages", "r") as f:
    for line in f:
        if "ERROR" in line:
            errors.append(line.strip())

print(f"Znalezione errory:", len(errors))