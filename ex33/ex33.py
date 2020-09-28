i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

def whiler(num, increment_val):
    i = 0
    numbers = []

    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + increment_val
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


whiler(10, 1)
whiler(12, 5)


numbers = []
for i in range(6):
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
