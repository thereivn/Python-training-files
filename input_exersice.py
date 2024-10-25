username = input("Enter a username: ")

username.find(" ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces!")
elif not username.isdigit() == -1:
    print("Your name can't contain a digit!")
else:
    print(f"Welcome {username}")