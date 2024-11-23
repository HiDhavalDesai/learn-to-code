#Hypotenuse of a right triangle.  
# C = sqrt(pow(a) *2 + pow(b)*2)

import math

A = float(input("What does side A measure? "))
B =  float(input("What does Side B measure? "))
C = math.sqrt(pow(A, 2) + pow(B,2))

print(f"The Hypotenuse is {round(C,2)}")