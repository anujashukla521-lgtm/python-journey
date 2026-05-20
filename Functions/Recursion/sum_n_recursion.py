# A recursive Python program that calculates the sum of natural numbers from 1 to n using a recursive function.

def total(num):
    add = 0
    if num == 0:
        return 0
    else:
        return num+total(num-1)

n = int(input("Enter a num: "))
addition = total(n)
print(f"Sum of {n} numbers: {addition}")