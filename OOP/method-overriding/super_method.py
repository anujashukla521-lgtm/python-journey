class Person:
    def show(self):
        print("Person details")

class Employee(Person):
    def show(self):
        super().show()
        print("Employee details")

emp = Employee()
emp.show()