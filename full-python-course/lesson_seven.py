#logical operators = evaluate multiple conditions (or, and , not)
#           or = at least one condition must be True
#           and = both conditions must be True
#           not = inverts the condition (not False = True, not True = False)

# Or operator - only one needs to be true
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The Outdoor event is still scheduled")
# The purpose of this is to check if the temp meets the conditions of being either greater than 35 or less than 0 or if it's raining.


# And operator, both conditions need to be true
temp_2 = 20
is_sunny = False

if temp_2 >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp_2 <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif temp_2 < 28 and temp_2 > 0 and is_sunny: 
    # another way to do this is 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
    # inverts the condition.
elif temp_2 >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is cloudy")
elif temp_2 <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif temp_2 < 28 and temp_2 > 0 and not is_sunny: 
    print("It is warm outside")
    print("It is cloudy")

