credit_number = "1234-5678-9012-3456"

# indexing - accesing element of a sequence using [ (indexing operator)]
#[start : end : step]
# print(credit_number[0 : 4 : 2])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[10:])
# print(credit_number[-1])
# print(credit_number[::2])
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

#REVERSED
last_digits = credit_number[::-1]
print(last_digits)