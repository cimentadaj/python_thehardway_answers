print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy")


# Study drills
print("Are you familiar with Mario?", end=' ')

if (input()):
    print("Then you are in for a treat!")
    print("I love Mario!")
    print("What age did you first play it?", end=' ')
    if (int(input()) < 11):
        print("Wow, you did before me, that's neat!")
    else:
        print("Ahh, I was playing back then.")

else:
    print("That's too bad, you should download it soon!")
