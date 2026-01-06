numbers = []

while True:
    x = input("Podaj liczbę (q aby wyjść): ")

    if x == "q":
        break

    numbers.append(int(x))

print("Liczby: ", numbers)
print("Suma tych liczb wynosi: ", sum(numbers))
print("Średnia liczb: ", sum(numbers) / len(numbers))
