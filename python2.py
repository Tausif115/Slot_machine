row = int(input("Enter the number of rows: "))
coloumn = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")


for y in range(row):
    for x in range(coloumn):
        print(symbol, end=" ")
    print()


