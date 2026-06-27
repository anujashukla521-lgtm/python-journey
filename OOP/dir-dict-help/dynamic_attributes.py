class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

emp = Employee("Nitin", 20000)
emp.display()
print(emp.__dict__)
emp.department = "HR"
print(emp.__dict__)
