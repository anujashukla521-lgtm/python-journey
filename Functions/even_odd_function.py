# A Python function that checks whether a number is even or odd using conditional statements.

def numChecker(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a num: "))
x = numChecker(num)
print("Number is:",x)
