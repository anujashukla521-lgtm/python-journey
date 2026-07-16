secret_number = 7

while (number:=int(input("Enter a number: ")))!=secret_number:
    print("Wrong guess")

print("You got right, number is",secret_number)
