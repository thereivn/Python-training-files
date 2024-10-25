# format specifiers = {value:flags} format a value based on what flags are inserted

import os
import msvcrt

os.system("cls"); print("\n")

price1 = 3.1415
price2 = -987.65
price3 = 12.34

# ограничитель
print(f"Price 1 is {price1:.1f}")
print(f"Price 2 is {price2:.1f}")
print(f"Price 3 is {price3:.1f}")
print("\n")
# ограничитель
print(f"Price 1 is {price1:+,.2f}")
print(f"Price 2 is {price2:+,.2f}")
print(f"Price 3 is {price3:+,.2f}")
print("\n")

print("Ожидание нажатия клавиши...")
msvcrt.getch()