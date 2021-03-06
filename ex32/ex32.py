the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type {fruit}")

# also we can do through mixed lists
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# or just do this
elements = list(range(0, 6))

for i in elements:
    print(f"Element was: {i}")
