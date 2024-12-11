#while loop = execute some code while some condition remains true

name = input("Enter Your Name: ")
while name == "":
    print("You did not enter your name, please enter your name")
    name = input("Enter Your Name: ")
print(f"Hello {name}")
# age = input("How old are you? ")


# For as long as the while loop is true, it will repeat. Once it's false, only then will the second part run. Spacing matters.
# if we remove the input that is prompted again, (line 6), then we will have an infinite-loop.

# Using Age
age = int(input("How old are you? "))

while age <= 0:
    print("Age can't be negative or zero")
    age = int(input("How old are you? "))
print(f"you are {age} years old")


# Adding logical operators

food = input("Enter a food you like (q to quit)")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit)")

print("bye")

#or logical operator

num = int(input("Enter a number between 1 - 10: "))
while num <1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")