#if statement in python
import os
import keyboard
import msvcrt

os.system("cls"); print("\n")

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are signed up!")
elif age <= 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up!")

print("Ожидание нажатия клавиши...")
msvcrt.getch()