#variables = A container for a value (string, integer, float, boolean)
#   A variable behaves as if it was the value it contains

#Strings - Are between quotes
first_name = "John"
print(first_name)
food = "pizza"
email = "cool@gmail.com"

# You don't want to just write it as print("first_name"), because this will just print first_name 
# You can use your variable along with some text, using what is called an f-string. 
# To use formatted string literal, beginning a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a python expression between ( and ) characters that can refer to variables or literal values.

print(f"Hello {first_name}")
# f means format
print(f"you like {food}")
print(f"Your email is {email}")


#Integers - whole number, age (example)
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")


#Float (has a decimal)
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"You GPA is: {gpa}")
print(f"You ran {distance}KM")

#Booleans - is either True or False
is_student = True
for_sale = False
is_online = False

print(f"Are you a student: {is_student}")
# If-statement with a boolean
if is_student:
    print("Yes, I am a student")
else :
    print("No I am not a student")

if for_sale:
    print("The Car is for sale")
else:
    print("The car is not for sale")

if is_online:
    print("You are Online")
else:
    print("You are offline")