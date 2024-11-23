# if = do some code only IF someone condition is true
#   Else do something else

age = int(input("Enter your age: "))

if age >=18 and age < 100:
    print("You are now signed Up")
elif age <0:
     print("You haven't been born yet!")
elif age >=100:
    print("You are too old to sign up!")
else:
    print("You must be 18+ to sign Up")

# Food Exercise:
#  == is a comparison operator and will check to see if two values are equal, o one = means variable.

response = input("Would you like some food? (Y/N): ")

if response == "Y" or response == "y":
    print("Here is your food")
elif response == "N" or  response == "n":
    print("Okay, No food for you.")
else:
    print("I don't know what that means.")



# Booleans with if-statements

for_sale = True
# False will trigger else.

if for_sale:
    print("Yes, It's for sale")
else: 
    print("It's not for sale.")