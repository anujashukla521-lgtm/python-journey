class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self,name,age,roll_no):
        Person.__init__(self,name,age)
        self.roll_no = roll_no

    def display(self):
        print(f"Roll no: {self.roll_no}")

class Employee(Person):
    def __init__(self,name,age,employee_id):
        Person.__init__(self,name,age)
        self.employee_id = employee_id

    def display(self):
        print(f"Employee ID: {self.employee_id}")

class TeachingAssistant(Student,Employee):
    def __init__(self,name,age,roll_no,employee_id,subject):
        Student.__init__(self,name,age,roll_no)
        Employee.__init__(self,name,age,employee_id)
        self.subject = subject
    
    def display(self):
        Person.display(self)
        Student.display(self)
        Employee.display(self)
        print(f"Subject: {self.subject}")
        

teacher = TeachingAssistant("Striver",39,101,121,"DSA")
teacher.display()

