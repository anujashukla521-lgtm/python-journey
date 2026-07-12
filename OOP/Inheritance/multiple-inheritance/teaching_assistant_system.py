class Person:
    def __init__(self,name,**kwargs):
        self.name = name
        super().__init__(**kwargs)

class Employee(Person):
    def __init__(self,salary,**kwargs):
        self.salary = salary
        super().__init__(**kwargs)

class Student(Person):
    def __init__(self,course,**kwargs):
        self.course = course
        super().__init__(**kwargs)

class TeachingAssistant(Employee,Student):
    def __init__(self, name, salary, course):
        super().__init__(
            name=name,
            salary=salary,
            course=course
        )

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Course: {self.course}")



teach = TeachingAssistant(name="Vikrant",salary=20000,course="BTech")
teach.display()
