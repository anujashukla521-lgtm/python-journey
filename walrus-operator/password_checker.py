set_password = "python123"

while (password:= input("Enter password: "))!=set_password:
    print("Wrong password, try again")

print("You passoword is correct",set_password)