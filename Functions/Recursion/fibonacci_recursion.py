# A recursive Python program that generates and displays the Fibonacci sequence up to a user-specified number using a user-defined recursive function.

def fibonacci(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num = int(input("Enter a num: "))
for i in range(num):
    print(fibonacci(i),end=" ")