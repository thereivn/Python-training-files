import os
import msvcrt

os.system("cls"); print("\n")

name = input("Enter name: ")

# result = len(name) # <- длина стринг
result = (name.find("")) # <- нахождение символа с начала
result = (name.rfind("o")) # <- reversed с конца нахождение символа
name = name.capitalize()

print(result)
print(name)

print("Ожидание нажатия клавиши...")
msvcrt.getch()