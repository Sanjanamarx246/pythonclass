# program to check password and
#Make sure it is 8 characters long
username = input("Enter your name: ")
password = input("enter your password: ")
passwordLength = len(password)
while passwordLength < 8:
    print("Password must be more than 8 character")
    password = input("Enter your password: ")
    passwordlength = len(password)

hiddenPassword= '*' * len(password)
print(f"Hello {username} your password is {hiddenPassword}")