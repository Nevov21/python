# def double(x):
#     return x * 2

# liczba = int(input("Podaj swoją liczbę: "))
# print(double(liczba))

def parzysta(y: int):
    return y % 2 == 0

for i in range(1 ,11):
    print(i, parzysta(i))