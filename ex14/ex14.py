from sys import argv

script, user_name, age = argv

prompt = "> Please answer here: "

print(f"Hi {user_name}, aged {age}, I'm the {script} script.")
print("I'd like to ask your a few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(
    f"""
    Alright, so you said {likes} about liking me.
    You lives in {lives}. Not sure where that is.
    And your have a {computer} computer. Nice.
    """
)
