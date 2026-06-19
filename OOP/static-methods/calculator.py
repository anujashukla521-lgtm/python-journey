# A utility class demonstrating static methods for performing basic arithmetic operations such as addition, subtraction, and multiplication without creating an object.

class Calculator:
    
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def subtract(a,b):
        return a-b

    @staticmethod
    def multiply(a,b):
        return a*b

print("Addition:", Calculator.add(15,7))
print("Subtraction:", Calculator.subtract(15,7))
print("Multiplication:", Calculator.multiply(5,7))

