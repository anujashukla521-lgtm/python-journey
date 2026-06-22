class Employee:
    employee_count = 0
    def __init__(self,name):
        self.name = name
        Employee.employee_count+=1

    def get_name(self):
        print(f"Name: {self.name}")

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count


emp1 = Employee("Harry")
emp2 = Employee("Ron")
emp3 = Employee("Hermoine")
emp4 = Employee("Luna")

emp1.get_name()
emp2.get_name()
emp3.get_name()
emp4.get_name()

print("Total employee:",Employee.get_employee_count())