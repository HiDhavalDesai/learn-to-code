#Temperature Conversion program
# ° is degrees alt + 0176

unit = input("Is this temperature in Celsius or Fahrenheit? ")
temp = float(input("What is the temperature? "))

if unit.upper() == "F" or unit.upper() == "FAHRENHEIT":
    new_temp = round((temp - 32) *(5/9), 1)
    print(f"{temp} is {new_temp}°C")
elif unit.upper() == "C" or unit.upper() == "CELSIUS":
   new_temp =  round((temp * (9/5)) +32, 1)
   print(f"{temp} is {new_temp}°F")
else:
    print(f"{unit} is not valid. Please try again.")