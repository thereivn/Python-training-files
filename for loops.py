import os
import msvcrt

os.system("cls"); print("\n")

# for x in reversed(range(1, 11, 2)):
#     print(x)
# print("HAPPY NEW YEAR!")

# credit_card = "1234-5678-9123-1234"

# for x in credit_card:
#     print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

print("Ожидание нажатия клавиши...")
msvcrt.getch()