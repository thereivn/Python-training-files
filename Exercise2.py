#Shopping cart program
import os

os.system("cls"); print("\n")

item = str(input("What item would you like to buy: "))
price = float(input("What is the price: "))
quantity = int(input("How many?: "))

total = price * quantity
print(f"So price of yours {quantity}'s {item}'s will be {total}$")