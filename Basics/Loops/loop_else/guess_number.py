# A Python number guessing game that gives the user limited attempts to guess a secret number using a while loop with else.

secret_num = 7
attempts = 0
while attempts<5:
    guess = int(input("Enter num: "))
    if secret_num == guess:
        print("You won")
        break
    attempts+=1

else:
    print("You lost")
