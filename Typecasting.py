# Typecasting, p.s. процесс конвертации переменных одного типа в другой (str(), int(), float(), bool())

import os

os.system("cls")
print(" \n")

name = "Misso Sino"
age = 20
score = 5.55
student = True

print(type(name))
print(type(age))
print(type(score))
print(type(student))

score = int(score)
print(score)

age = float(age)
print(age)

age = str(age)
print(age ,type(age))
# age +=1 is not what might be
age += "1" # is may be
print(age)

name = bool(name)
print(name)

