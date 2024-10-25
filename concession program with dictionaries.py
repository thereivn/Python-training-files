import os

os.system("cls"); print("\n")

menu = {"pizza":3.00,
        "nachos":4.50,
        "popcorn":6.50,
        "fries":7.50,
        "chiken":8.50,
        "chips":3.50,
        "soda":2.50,
        }

cart = []
total = 0

print("------------------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print()
for food in cart:
    total += menu.get(food)
    print("In your Order: ")
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")