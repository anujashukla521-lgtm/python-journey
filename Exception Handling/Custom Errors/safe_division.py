# Performs division between two numbers while handling invalid input and division-by-zero errors using exception handling.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1/num2)
except ValueError:
    print("Invalid number input")
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print("Program ended")
