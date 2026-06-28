class Person:
    def __init__(self):
        print("Parent method called")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Child method called")

emp = Employee()