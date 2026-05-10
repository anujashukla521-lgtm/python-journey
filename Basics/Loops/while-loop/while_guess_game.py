# A simple number guessing game using a while loop that keeps asking the user until the correct number is guessed.

num = int(input("Enter num: "))
guess = int(input("Guess the num: "))
while guess != num:
    guess = int(input("Guess the num: "))
    print("Try again")
else:
    print("Success")
