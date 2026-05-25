# Validates user age input and raises custom errors for ages outside the allowed range using exception handling.

try:
    age = int(input("Enter age: "))
    if age<5 or age>100:
        raise ValueError("Age out of valid range")
    else:
        print(f"Age is {age}")
except ValueError as e:
    print(e)

finally:
    print("Program ended")
