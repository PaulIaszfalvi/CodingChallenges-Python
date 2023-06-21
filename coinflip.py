import random

for x in range(100):
    number = random.randint(1, 2)

    if number == 1:
        print("Head")
    else:
        print("Tail")