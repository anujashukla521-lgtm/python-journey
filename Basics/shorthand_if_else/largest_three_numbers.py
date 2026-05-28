# Finds the largest number among three inputs using nested shorthand if-else.

num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
print(f"{num1} is greatest") if num1>num2 and num1>num3 else print(f"{num2} is greatest") if num2>num1 and num2>num3 else print(f"{num3} is greatest")
