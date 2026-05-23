# Takes two numbers from the user and performs division while handling errors like invalid input and division by zero using exception handling.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1/num2)
except ValueError:
    print("Invalid number input")
except ZeroDivisionError:
    print("Can't divide by zero")
