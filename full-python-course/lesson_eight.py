# Conditional Expressions = A one-line shortcut for the if-else statement (ternary operator)
#               Print or assign one of two values based on a condition
#               Formula - X if condition else Y
#                   if condition is true run x else y

num = 1
print("Positive" if num > 0 else "negative")
# This is combining the if-else statement. So if the num variable is positive (greater than 0), it will print positive, else if the num is negative (less than 0) it will print negative.

num_2 = 13
result = print("Even" if num_2 % 2 == 0 else "Odd")
#               The first value is true and the second one is false.

num_3 = 5
a = 8
b = 5
age = 17
temperature = 20
user_role = "Admin"
max_num = print(a if a>b else b)
min_num = print(a if a<b else b)

status = print("Adult" if age >= 18 else "Child")
weather = print("Hot" if temperature > 20 else "Cold")

access_level = print("Full Access" if user_role == "Admin" else "Limited Access")
#           return the text of full access if our condition of user_role is equal to a string admin else we will return limited access.

# TestforSelf

temp_hot = 80
temp_cold = 50

whether_app = print("it's nice out" if temp_hot >= 50 or temp_cold <=50 else "not nice out")