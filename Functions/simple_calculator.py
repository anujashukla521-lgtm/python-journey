# A mini calculator built using multiple functions to perform arithmetic operations like addition, subtraction, multiplication, and division.

def addition(x,y):
    print("Addition:",x+y)
def subtraction(x,y):
    print("Subtraction:",x-y)
def multiplication(x,y):
    print("Multiplication:",x*y)
def division(x,y):
    print("Division:",x/y)

a = int(input("Enter first num: "))
b = int(input("Enter second num: "))

addition(a,b)
subtraction(a,b)
multiplication(a,b)
division(a,b)
