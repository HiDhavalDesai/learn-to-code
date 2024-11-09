#variables = A container for a value (string, integer, float, boolean)
#   A variable behaves as if it was the value it contains

#Strings - Are between quotes
first_name = "John"
print(first_name)
food = "pizza"
email = "cool@gmail.com"

# You don't want to just write it as print("first_name"), because this will just print first_name 
# You can use your variable along with some text, using what is called an f-string. 
# To use formatted string literal, bein a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a python expression between ( and ) characters that can refer to variables or literal values.

print(f"Hello {first_name}")
# f means format
print(f"you like {food}")
print(f"Your email is {email}")


#Integers - whole number, age (example)
age = 25


print(f"You are {age} years old")


#Float


#Booleans