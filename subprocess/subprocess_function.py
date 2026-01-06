import subprocess

result = subprocess.run(["ls", "-ltra"], capture_output=True, text=True)
print(result.stdout)



result = subprocess.run(["systemctl","is-active","ssh"], capture_output=True, text=True)

if result.stdout != "active":
    print("SSH NIE DZIAŁA!", result.stdout)
