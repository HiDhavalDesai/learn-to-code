#Python Compound Interest Calculator
# Formula is A = P(1 + r/n)^t

principal = float(input("What is the initial balance? "))
while principal <= 0:
    principal = float(input("What is the initial balance? "))
    if principal <= 0:
    print("Principal balance cannot be less than or equal to zero.")
print(f"The initial amount is {principal}")

# rate = float(input("What is the rate? "))
# time = int(input("For how long (in years) "))



# final_amt = principal (1+rate/n)**time