# For loops = Execute a block of code a fixed number of times.
#              You can iterate over a range, string, sequence, etc.

for x in range(1,11):
    print(x)
# for x(variable) in the range of numbers 1 to 11, where 11 is excluded

for count in reversed(range(1,11,2)):
    print(count)
print("Happy New Year!")
# This will reverse the count, but then the 2 in the range is a step count, so you will count by 2s backwards.

credit_card = "1234-5432-2135-4321"

for x in credit_card:
    print(x)
# X will hold the position, and then will list out each number in the credit card variable.

# continue
for x in range(1,21):
    if x ==13:
        continue
    else:
        print(x)
# Using continue we are skipping 13, and then we continue with the count.

# Break - It will break the loop before we hit 13, so we break at 12
for x in range(1,21):
    if x ==13:
        break
    else:
        print(x)