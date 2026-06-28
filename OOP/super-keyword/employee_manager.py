class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

manager = Manager("Binod",300000,"HR")
manager.display()