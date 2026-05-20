# A recursive Python program that calculates the power of a number by repeatedly multiplying the base until the exponent becomes 0.

def power(x,n):
    if n == 0:
        return 1
    else:
        return x*power(x,n-1)

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
power_func = power(base,exponent)
print(power_func)