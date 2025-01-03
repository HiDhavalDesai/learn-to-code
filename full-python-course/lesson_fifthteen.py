# Collection = Single "variable" use to store multiple values
#   List = [] ordered and changeable. Duplicates Ok.
#   Set = {} unordered and immutable, but add/remove ok. No duplicates
#   tuple = () ordered and unchangeable. Duplicates ok. Faster
# There are also dictionaries, but we will review that for later.

fruits = ["Apple","Orange","Banana","Coconut"]
# print(dir(fruits))
# This function here gives you all the attributes.
# print(help(fruits))
# This gives you a definition of all the attributes and what you can do.

# each value in a collection is also known as a element.
print(fruits[::-1])
# [] is an index operator. adding [0] will print apple, [1] will print orange; you can also set a beginning index, an ending index and a step.

for fruit in fruits:
    print(fruit)

print(len(fruits))

print("Apple" in fruits)
# This is a boolean, if true, then yes the value is in the list.


# fruits[0] = "pineapple"
# We are saying let's replace the element in place 0 with pineapple.

# for fruit in fruits:
#     print(fruit)

# methods-

fruits.append("pineapple")
# append will add an element to the list

fruits.remove("Apple")
# to remove an element you can use remove

fruits.
# 

print(fruits)
