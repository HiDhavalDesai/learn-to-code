# Validate user input exercise
# Username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

username = input("Enter Your Username: ")
len(username)
count = len(username)
if count > 12:
    print("username is more than 12 characters, please try again.")
elif not username.isalpha():
    print("There are spaces or numbers in the username, please try again.")
else:
    print("Username is valid.")