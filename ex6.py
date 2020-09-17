# Here we write the number of type of people and use that inside
# the formatted string in `x`
types_of_people = 10
x = f"There are {types_of_people} types of people."

# Same as before. We define two variables and use
# them inside a formatted string
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

# Print the two formatted strings from above
print(x)
print(y)


# Create two new f-strings with the two f-strings from above
print(f"I said {x}")
print(f"I also said '{y}'")

# Define a boolean
hilarious = False

# Define a normal string (without an f-string, such that {} is NOT passing a
# variable)
joke_evaluation = "Isn't that joke so funny?! {}"

# Format that string with a method rather than with an f-string
print(joke_evaluation.format(hilarious))

# Create two strings
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate them. The sep here is '' rather than ' '
print(w + e)

# For example, the same thing can be achieved without the +
print(w, e, sep="")


# Study drills
# 1. write a comment above each line
# done

# 2. Find all strings inside another string
# using f-string there are 4 but using format there are 5

# 4. why adding + makes two strings longer
# because it concatenates them
