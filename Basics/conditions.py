# This file includes beginner-level Python programs demonstrating conditional statements (if, elif, else) to perform logical checks such as even/odd, number comparison, sign detection, and divisibility.

# Program 1: Even/Odd
n = int(input("Enter a number:"))
if n%2==0:
    print(n, "is an even number.")
else:
    print(n, "is a odd number.")

# Program 2 : Positive/Negative/Zero
n = int(input("Enter a number: "))
if n==0:
    print(n, "is zero.")
elif n>0:
    print(n, "is positive.")
else:
    print(n, "is negative.")

# Program 3 : GreaterNumber
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
if m>n:
    print(m, "is greater than",n)
elif m<n:
    print(n, "is greater than",m)
else:
    print("Both are equal")

# Program 4 : Divisibility by 3 and 5 both
n = int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print(n, "is divisible by both 3 and 5.")
else:
    print(n, "is not divisible by both 3 and 5.")