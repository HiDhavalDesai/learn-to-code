# Create a rectangle using symbols.

rows = int(input(" Enter the number of rows: "))
columns = int(input(" Enter the number of columns: "))
symbol = input("Enter a symbol: ")

# outer loop is in charge of the rows.
# Inner loop is in charge of the columns.

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()