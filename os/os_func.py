import os

print(os.getcwd())
print(os.listdir("."))

if os.path.exists("/etc/passwd"):
    print("Ścieżka istnieje!")
else:
    print("Ścieżka nie istenieje!")

os.makedirs("backup", exist_ok=True)