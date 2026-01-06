import random

numbers = [1, 2, 3, 4]
names = ["Ala", "Jacek", "Kasia"]
mixed = [1, "Jacek", True]

print(numbers)
print(names)
print(mixed)

numbers.append(5)
numbers.remove(2)
numbers[0] = 100

# print(numbers)
# print(f"Długość listy:", len(numbers))

# while len(numbers) < 10:
#     numbers.append(random.randint(1, 10))
#     print(numbers)

for i in numbers:
    print(i)