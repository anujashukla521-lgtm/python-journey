# Performs basic arithmetic operations using functions while handling invalid operations, wrong input, and division-by-zero errors.

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def product(a,b):
    return a*b

def division(a,b):
    return a/b

while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operation = input("Enter operation to perform: ")
        if operation == "+":
            result = addition(num1,num2)
            print(result)
        elif operation == "-":
            result = subtraction(num1,num2)
            print(result)
        elif operation == "*":
            result = product(num1,num2)
            print(result)
        elif operation == "/":
            result = division(num1,num2)
            print(result)
        else:
            raise ValueError("Invalid operation")


    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Can't divide by zero")

    finally:
        print("Operation ended")

    choice = input("Continue? y/n:")
    if choice.lower() == "n":
        break
