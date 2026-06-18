class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def manager_info(self):
        print(f"Department: {self.department}")
name = input("Enter name: ")
salary = float(input("Enter salary: "))
department = input("Enter department: ")
try:
    m1 = Manager(name,salary,department)
    m1.showDetails()
    m1.manager_info()
except ValueError as e:
    print(e)