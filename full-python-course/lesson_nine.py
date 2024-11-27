# String Methods
#  A string is just a series of characters

name = input("Enter your full name: ")


# Function = length. Give you the length of the string, how many characters.
# Length starts with 1 and then counts the number of characters till the end; for name Donkey, it is 6 characters; whitespace counts.

char_length =len(name)
print(char_length)

# if we enter our variable and then enter dot (.) we access different kinds of methods.
# the find method find the first occurrence of that character. so for donkey, if you look for the y, it will tell you the y is in the 5th position, this is because find starts at 0, 0 being the first character.
name_2 = name.find("y")
print(name_2)

# For the reverse(r) or the Last occurrence of the string, you do rfind; the lasts time that letter appears. For Donkey Kong, if you look for o, it will be 8
name_3 = name.rfind('o')
print(name_3)
# if you want to search for the character a the character is not found in the string, then it will display -1.

# capitalize function, is done with (.)dot capitalize; since donkey kong is one string, you it will only capitalize the first letter of the word 
name_upp = name.capitalize()
print(name_upp)

# upper method will make everything uppercase in the string.
upp_name = name.upper()
print(upp_name)

# lower make the words all lowercase
lower_name = name.lower()
print(lower_name)

#isdigit method will give either true or false; its checking to see if a string contains only digits. If the string is all numbers (digits) then it will display true, if the string is numbers and letters, it will display false, if it's just letters it will display false.
digits = name.isdigit()
print(digits)

# isalpha, this will display either true or false; if the string contains only alphabetic characters it will display true, if it has numbers and letters then it will display false, and if it has numbers only it will display false. whitespace or space makes is not an alphabetic character.
alpha =name.isalpha()
print(alpha)

# Numbers / Phone Numbers
# Count how many dashes are going to be in the phone; the count method will count the number of that character. dash_count will give us an integer
phone_number = input("Enter your phone number :")
dash_count = phone_number.count("-")
print(dash_count)


# replace method, we can replace all occurrence with another character.
# Fox example, we can replace all the dashes from the phone number and replace them with an empty string; this will remove the - and then you will be left with a phone number and no space.
free_number = phone_number.replace('-','')
print(free_number)

# Helper methods, print(help(str))
print(help(str))