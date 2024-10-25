import os
import msvcrt

os.system("cls"); print("\n")

temp = 36
is_raining = True

if temp > 35 and is_raining:
    print("The outdoor event is canceled")
else:
    print("...")

print("Ожидание нажатия клавиши...")
msvcrt.getch()