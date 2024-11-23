# Find the circumference of a circle
import math

# circumference = 2 pi r

radius = float(input("What is the radius of the circle? "))

circumference = 2 * math.pi * radius
print(f"The radius of {radius} gives us a circumference of {circumference}")
# If you want to round the solution, you can do round(variable, (number of digits))  This would look like {round(circumference,2)}