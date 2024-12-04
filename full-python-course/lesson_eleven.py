#format specifier = {value:flag} format a value based on what 
#                           flags are inserted

# .(number)f = round to that many decimal places (fixed point)
#  :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# : ^ = center align
# : + = use a plus sign to indicate positive value
# : = = place sign to leftmost position
# :  = insert a space before positive number
# :, = comma separator 


price_1 = 3.14159
price_2 = -987.65
price_3 = 12.34

print(f"Price 1 is ${price_1:.3f}")
print(f"Price 2 is ${price_2:.3f}")
print(f"Price 3 is ${price_3:.3f}")
# The above will give you that many decimal places after

print(f"Price 1 is ${price_1:10}")
print(f"Price 2 is ${price_2:10}")
print(f"Price 3 is ${price_3:10}")
# The above will give you the total number of characters, including spaces for that printout;
#  if you added a 0 before the 10, 010; the numbers would be 0-padded, see below
print(f"Price 3 is ${price_3:010}")

print(f"Price 1 is ${price_1:<10}")
# This will left justify the number, and the space would be after

print(f"Price 2 is ${price_2:>10}")
#This is right justified; and the spaces would be before this, also this is the default.

print(f"Price 3 is ${price_3:^10}")
#This is center aligned

print(f"Price 1 is ${price_1:+}")
print(f"Price 2 is ${price_2:+}")
print(f"Price 3 is ${price_3: }")
# If you have a positive value and wanted to display it, just use +, if the number is already negative, the negative will stay.
# The numbers will remain evenly spaced, if you remove the positive and just enter a space it will do the same thing

price_4 = 10000.58596
print(f"Price 4 is ${price_4:+,.2f}")
# A thousand separator is just a comma; this is also a combination of both


