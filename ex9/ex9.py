
# Collapse all days/months into a single string.
# However, \n signals a new line and if you print it
# it will get rendered as a new line.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Print both days and months
print("Here are the days:", days)
print("Here are the months:", months)

# Using """ allows you to use new lines
# and they're interpreted as that

print(
    """
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
    """
)

