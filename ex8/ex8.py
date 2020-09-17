# Create a string with four placeholders for format
formatter = "{} {} {} {}"

# Fill the four placer folders with 1 2 3 4
print(formatter.format(1, 2, 3, 4))

# Fill the four placer folders with one, two, three, four.
# Note that you can as many names as you want: if you only
# have four placer holder, formatter will only grab
# the number of arguments as placeholders
print(formatter.format("one", "two", "three", "four"))

# Fill out the place holders as booleans
print(formatter.format(True, False, False, True))

# Fill out each placeholder with the four {} (brackets)
# This will total a total of 16 brackets (4 place holders by
# 4 brackets each).
print(formatter.format(formatter, formatter, formatter, formatter))

# Fill out the four placeholders with four pphrases. For this
# look pretty we should avoid capital letters at the beginning
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
