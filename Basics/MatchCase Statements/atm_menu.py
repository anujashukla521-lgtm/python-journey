# Simulates a simple ATM menu using match-case statements.

num = int(input("Enter number: "))
match num:
    case 1:
        print("Check balance")
    case 2:
        print("Deposit")
    case 3:
        print("Withdraw")
    case 4:
        print("Exit")
    case _:
        print("Wrong input")