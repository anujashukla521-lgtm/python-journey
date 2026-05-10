num = int(input("Enter num: "))
guess = int(input("Guess the num: "))
while guess != num:
    guess = int(input("Guess the num: "))
    print("Try again")
else:
    print("Success")