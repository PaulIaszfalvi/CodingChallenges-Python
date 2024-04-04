import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_numbers = [random.randint(1, 100) for _ in range(10)]

print(random_numbers)

print(max(x for x in numbers))
print(max(x for x in random_numbers))