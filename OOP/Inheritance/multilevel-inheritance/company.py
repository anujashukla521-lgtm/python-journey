class Company:
    def __init__(self,company_name):
        self.company_name = company_name


class Department(Company):
    def __init__(self,company_name,department_name):
        super().__init__(company_name)
        self.department_name = department_name

class Employee(Department):
    def __init__(self,company_name,department_name,monthly_salary):
        super().__init__(company_name,department_name)
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return 12*float(self.monthly_salary)

    def display_info(self):
        print(f"Company name: {self.company_name}")
        print(f"Department name: {self.department_name}")
        print(f"Monthly salary: {self.monthly_salary}")
        print(f"Annual salary: {self.annual_salary()}")

emp = Employee("Amazon","HR","100000")
emp.display_info()
