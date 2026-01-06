import random

liczba = random.randint(1, 10)

while True:
    guess = int(input("Zgadnij jaka liczba jest wylosowana: "))

    if guess == liczba:
        print("Udało Ci się!")
        break
    elif guess > liczba:
        print("Za dużo!")
    else:
        print("Za mało!")

