class Person:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        Person.display(self)
        print(f"Subject: {self.subject}")

class MathTeacher(Teacher):
    def __init__(self,name,subject,experience):
        super().__init__(name,subject)
        self.experience = experience

    def display(self):
        Teacher.display(self)
        print(f"Experience: {self.experience}")

teacher = MathTeacher("Harry","Maths",5)
teacher.display()
