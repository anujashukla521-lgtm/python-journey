password = "python123"
attempts = 0
while attempts<3:
    guess = input("Enter password: ")
    if password == guess:
        print("Login successful")
        break
    attempts+=1

else:
    print("Account locked")