import os
import msvcrt

os.system("cls"); print("\n")

num = 5
a = 6
b = 7
age = 25
temp = 30

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
print(max_num)

status = "Adult" if age >= 18 else "Child"
print(status)

# weather = "HOT" if temp > 20 else "COLD"


print("Ожидание нажатия клавиши...")
msvcrt.getch()