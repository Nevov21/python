with open("test.txt", "a") as f: # a to jest append czyli dodaje kolejne linijki do pliku, jeżeli zamiast "a" będzie "w" to jest truncate pliku
    f.write("\nsiemka")

with open("test.txt", "r") as f: # "r" jest do odczytywania pliku 
    for line in f:
        print(line.strip())