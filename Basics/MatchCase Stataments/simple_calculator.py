# Performs basic arithmetic operations using match-case.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter operation to perform(+,-,*,/): ")
match op:
    case '+':
        print("Addition: ",x+y)
    case '-':
        print("Subtraction: ",x-y)
    case '*':
        print("Multiplication: ",x*y)
    case '/':
        print("Division: ",x/y)
    case _:
        print("Invalid operation")