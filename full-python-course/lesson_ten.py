# String Indexing =  accessing elements of a sequence using [] (indexing operators)   [start: end: step]

credit_card_number = "1234-5678-9012-3456"
# The first index is 0

print(credit_card_number[4])
# There are three fields the start, end and step; if you only enter 1 number, it is assumed that it is the starting position.

print(credit_card_number[0:4])
# This will print out the first 4 numbers. we are saying start at the first spot and then go to the fourth spot. The ending index is exclusive, meaning that it stops at the 3rd spot and only display those numbers.

print(credit_card_number[5:9])
# This will print the fifth place number to the ninth place number.


print(credit_card_number[5:])
# We want the last 12 digits; you will then start on the left, and count to what you want to omit and then enter that number colon. which will give you all the numbers after to the end.

print(credit_card_number[-1])
# To get the last character in the string, you will just do -1 and it will give you the last character. -2 is 5, -3 is 4..

print(credit_card_number[::3])
# Step is a way of count, for example step 2 means that you want every second number, by 3s means that you want every third number.


# Create a program to only get the last 4 digits of a credit card number.

cc_num = input("What is your credit card number :")
print(cc_num[-4:])

# Reverse the credit card number / string
rstring = input("What string do you want to reverse :")
print(rstring[::-1])
# The step being negative 1, which reverses the string.
