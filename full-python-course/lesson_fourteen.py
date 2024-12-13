# Nested Loop = A Loop within another loop (outer, inner)
#                   Outer loop:
#                       inner loop:
#  You can have a while loop inside of a while loop; a for loop inside of a for loop; a for loop inside of a while loop; a while loop inside of a for loop.

for x in range(3):
# Whatever is in this for-loop will occur 3 times. Instead of just writing 3, you can add 1,4 to do the same thing.
    for y in range(1,10):
     print(y, end="")
    print()
# for x in range(1,10):
#     print(x, end="")
# This is a loop created to just write 1-9 numbers, if we don't want it to list out the numbers, we can do print(x, end=""), this will write on the numbers left to right on one line.

# to repeat this 3 times, we can just nest another loop.