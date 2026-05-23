# Validates user input for age by ensuring it is numeric and within a realistic range, handling invalid input using exception handling.

try:
    age = int(input("Enter age: "))
    if age<0:
        print("Age can't be negative")
    elif age>120:
        print("Age can't exceed 120")
    else:
        print("Age is:",age)
except ValueError:
    print("Age must be numeric")
