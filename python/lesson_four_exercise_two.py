# Exercise - shopping cart program

item = str(input("What would you like to purchase? "))
price = float(input(f"What is the price of {item}? "))
quantity = int(input(f"How many {item}(s) would you like to purchase? "))
total = price * quantity

print(f"You have purchased {quantity} {item}(s) at {price} each. Your total is ${total}.")
