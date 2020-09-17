# Import the argv class from the sys class
from sys import argv

# Unpack the arguments provided input the command line called
# to script and filename
script, filename = argv

# Open the connection today the filename provided
txt = open(filename)

# Print the contents of the filename
print(f"Here's your file {filename}:")
print(txt.read())

# Accept a new argument in the program
print("Type the filename again:")
file_again = input("> ")

# Open the connection to the file and read it.
txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()
