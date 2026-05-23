def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter operation: ")
    if operation == "+":
        result = addition(num1,num2)
        print(f"Addition of {num1} and {num2} is {result}")
    elif operation == "-":
        result = subtraction(num1,num2)
        print(f"Subtraction of {num1} and {num2} is {result}")
    elif operation == "*":
        result = multiplication(num1,num2)
        print(f"Multiplication of {num1} and {num2} is {result}")
    elif operation == "/":
        result = division(num1,num2)
        print(f"Division of {num1} and {num2} is {result}")
    else:
        print("Invalid operator")

except ValueError:
    print("Invalid numbers")
except ZeroDivisionError:
    print("Can't divide by zero")

