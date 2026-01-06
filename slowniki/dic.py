user = {
    "name": "Jacek",
    "age": 31,
    "admin": True,
}

print(f"Imie admina:", user["name"], "\n")

print("Klucze i wartosci obiektu 'user'")
for key, value in user.items():
    print(key, value)

print("Klucze obiektu 'user'")
for key in user.keys():
    print(key)

print("Wartości obiektu 'user'")
for value in user.values():
    print(value)