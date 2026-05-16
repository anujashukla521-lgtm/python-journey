# A function-based program that returns the square of a number and demonstrates the use of docstrings in Python.

def square(n):
    '''Takes a number from user and returns its square'''
    return n**2

num = int(input("Enter a num: "))
x = square(num)
print(f"Square of {num} is {x}")
print(square.__doc__)
