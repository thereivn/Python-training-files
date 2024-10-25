import os
import math

os.system("cls")
print("\n")

#first
# r = float(input(f"Enter the radius: "))
# c = 2 * math.pi * r
# print(f"The circumference is: {round(c, 2)}cm")

#second
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius,2)
# print(f"The area of the circle is: {round(area,3)}cm^2")

#third
a = float(input("Enter a parametr: "))
b = float(input("Enter b parametr: "))
c = math.sqrt(pow(a,2)+pow(b,2))
print(f"Gipotenuse is {round(c,3)}cm")