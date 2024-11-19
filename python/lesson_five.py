#Arithmetic operators
#Math Functions

#Arithmetic
# Addition

friends  = 0
friends = friends +1
# friends+=1
# This is an augmented assignment, it does the same thing as +1 friends
print(f"friends {friends}")


#subtraction
plants = 2
plants -=1
# Augmented assignment used
print(f"plants {plants}")


#multiplication
cell_phone = 2
# cell_phone = cell_phone * 3
# Augmented would be cell_phone*=3
cell_phone *=5
print(f"cell phones {cell_phone}")

#Division
onions = 20
onions /= 5
print(f"onions {onions}")

#exponents
candy = 5
candy **=2
print(f"candy {candy}")

#Modules
# This gives use the remainder of a division
# Very common to use this to get even or odd.
books = 10
books %= 4
print(f"books {books}")


# Math Related Functions
#   round(), rounds to the nearest whole integer
#   abs(), absolute value of a number
#   pow(), we need a base and exponent, something to the power of something. First number is base, second number is power
#   max() what is the max value
#   min() what is the minimum value

x = 3.14
y = -4
z = 5

result = round(x)
print(result)

result2 = abs(y)
print(result2)

result3 = pow(2,3)
# 2x2x2 2 to the 3rd power
print(result3)

max = max(x,y,z)
print(max)

min = min(x,y,z)
print(min)
