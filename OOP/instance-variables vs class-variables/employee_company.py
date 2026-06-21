# A Python program illustrating the difference between class variables and instance variables by managing employee company information and showing how instance-level changes differ from class-level changes.

class Employee:
    company = "Google"
    def __init__(self,emp_name):
        self.emp_name = emp_name

    def show(self):
        print(self.emp_name,"is working in",self.company)


emp1 = Employee("Gargi")
emp2 = Employee("Rohan")
emp1.company = "Amazon"
Employee.company = "Microsoft"
emp1.show()
emp2.show()
