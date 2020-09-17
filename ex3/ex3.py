# Print a string literal
print("I will now count my chickens:")

# Print both combination of math operators and strings. This means
# that python evaluates both arguments separately and prints them
print("Hens", 25 + 30 / 6.0)
print("Roosters", 100.0 - 25 * 3 % 4)

# Note that this means that the result is not a 'concatenated' string.
# It is rather just a print statement sent to stdout

print("Now I will count the eggs:")

# Printing a mathematical operation
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6.0)

print("Is is true that 3 + 2 < 5 - 7?")
print(3.0 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2.0)
print("What is 5 - 7?", 5 - 7.0)

print("Oh, that's why it's False")

print("How about some more?")

# It also prints logicals or just whatever you send it.
print("Is it greater?", 5 > -2.0)
print("Is it greater or equal?", 5 >= -2.0)
print("Is it less or equal?", 5 <= 2.0)

# You can print function bodies, for example.
print(sum)
