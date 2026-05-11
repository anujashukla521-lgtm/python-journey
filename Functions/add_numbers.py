# A basic function-based program that takes two numbers as input and returns their sum.

def add(x,y):
    return x+y

a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
total = add(a,b)
print("Addition: ",total)
