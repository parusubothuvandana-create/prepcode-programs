password = input("enter the password: ")
characters = int(input("enter the characters: "))

if characters >= 8 and "@" in password:
    print("password is  valid")
else:
    print("password is invalid")