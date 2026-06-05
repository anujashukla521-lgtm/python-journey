addition = lambda x,y: x+y
subtraction = lambda x,y: x-y
product = lambda x,y: x*y
division = lambda x,y: x/y

a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
print("Addition ",addition(a,b))
print("Subtraction ",subtraction(a,b))
print("Product ",product(a,b))
print("Division ",division(a,b))