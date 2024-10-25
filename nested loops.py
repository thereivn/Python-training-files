
import os

os.system("cls"); print("\n")

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter the # of symbol: ")

# for x in range(3):
#     for y in range(1,10):
#         print(y, end=" ")
#     print()

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
