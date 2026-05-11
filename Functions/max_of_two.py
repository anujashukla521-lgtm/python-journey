# A program that compares two numbers and returns the greater value without using built-in functions.

def maximum(x,y):
    if x>y:
        return x
    else:
        return y

m = int(input("Enter first num: "))
n = int(input("Enter second num: "))
a = maximum(m,n)
print(a)
