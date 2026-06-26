class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

    @classmethod
    def from_csv(cls,data):
        name,salary = data.split(",")
        return cls(name,float(salary))


emp1 = Employee.from_csv("Rahul,12200")
emp2 = Employee.from_csv("John,40000")
emp3 = Employee.from_csv("Rohit,20300")

emp1.display()
emp2.display()
emp3.display()