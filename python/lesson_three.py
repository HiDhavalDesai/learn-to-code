#typecasting = the process of converting a variable from one data type to another 
#       str(), int(), float(), bool()


name = "SuperMan"
age = 30
gpa = 3.4
is_student = True

type(name)
# This does not display the type that name is.

print(type(name))
# This does tell us the class type which is string.
# We can do that with all our variables.
# For age we would get int
# For gpa we would get float
# For is_student we would get bool


# Now we can convert one data type to another.
# GPA to integers

gpa = int(gpa)
print(gpa)
# output is 3

age = float(age)
print(age)
#It will print 30.0

age = str(age)
# age = age +1 and age+=1 are the same thing; this is not possible we get an error, because we can't add anything to a string; TypeError: can only concatenate str (not "int") to str
# to resolve this we can just do age+="1", this will allow the string to be added to a string.

print(age)
#This will make the age a string - so it will show "30"


name = bool(name)
print(name)
# We get True; as long as something is present, it will be true; if it was empty then it will give False.


# This is very important when handling user-input as it will always be a string.