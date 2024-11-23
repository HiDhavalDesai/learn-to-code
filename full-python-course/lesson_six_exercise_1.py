#Python Calculator
# This is a python calculator program.

# The user will select a arithmetic operator.

operator = input("Enter an operator (+ - * / %): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# If we don't turn these numbers into integers or floats, they are strings and we cannot use operators on them. 
# It's called string concatenation

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operator == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
else: 
    print("That is not an operator, please try again.")


