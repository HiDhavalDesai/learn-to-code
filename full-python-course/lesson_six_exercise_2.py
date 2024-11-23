#python Weight Converter
# We will convert kgs to lbs or lbs to kgs.

weight = float(input("Enter your weight: "))
unit = input("In Kilograms or Pounds? ")

if unit.upper() == "KILOGRAMS" or unit.upper() == "KGS":
    weight_conv = weight* 2.205
    result = print(f"{weight} in kgs is {weight_conv} in lbs")

elif unit.upper() == "POUNDS" or unit.upper() == "LBS":
    weight_conv = weight / 2.205
    result = print(f"{round(weight,2)} in lbs is {weight_conv} in kgs")

else:
    print(f"Please try again. {unit} is not a unit we can convert.")
