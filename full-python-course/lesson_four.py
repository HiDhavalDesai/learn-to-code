#input() = A function that prompts the user to enter data
#           Returns the entered data as a strong.

name = input("What is your name?: ")
age =  input("How old are you?: ")
# Another way of doing this is typecasting the input.
age = int(input("How Old are you?: "))
age = age +1
print(f"Hello {name}")
print("Happy Birthday!")
print(f"You are {age} year old!")