# A recursive Python program that calculates the factorial of a number using a user-defined function, handles negative number input, and displays the result using formatted output.

def factorial(n):
    if n<0:
        print("Factorial does not exist for negative numbers")
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


num = int(input("Enter a num: "))
fact = factorial(num)
print(f"Factorial of {num} is {fact}")