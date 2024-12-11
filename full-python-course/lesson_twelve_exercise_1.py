#Python Compound Interest Calculator
# Formula is A = P(1 + r/n)^t

principal = 0
time = 0
rate = 0

while principal <= 0:
    principal = float(input("What is the initial balance? "))
    if principal <= 0:
        print("Principal balance cannot be less than or equal to zero.")

while time <= 0:
    time = int(input("For how many years would you like to invest your money? "))
    if time <=0:
        print("Time cannot be less than or equal to zero years")

while rate <=0:
    rate = float(input("At what interest rate are you investing your money? "))
    if rate <=0:
        print("rate cannot be less than or equal to zero percent")

print(f"The initial amount is ${principal}")
print(f"We will invest your money for {time} years")
print(f"Your money will be invested at {rate} percent")

final_amount = principal * pow((1 + rate/100),time)

print(f"Your final amount will be ${final_amount:.2f}")