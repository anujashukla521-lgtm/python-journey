class Person:
    def __init__(self,name,**kwargs):
        self.name = name
        super().__init__(**kwargs)

class Teacher(Person):
    def __init__(self,subject,**kwargs):
        self.subject = subject
        super().__init__(**kwargs)

    def teach(self):
        print(f"{self.name} teaches {self.subject}")

class Coder(Person):
    def __init__(self,language,**kwargs):
        self.language = language
        super().__init__(**kwargs)

    def code(self):
        print(f"{self.name} codes in {self.language}")

class DeveloperTeacher(Teacher,Coder):
    def __init__(self,salary,**kwargs):
        self.salary = salary
        super().__init__(**kwargs)

    def details(self):
        self.teach()
        self.code()
        print(f"{self.name}'s salary is {self.salary}")
dev = DeveloperTeacher(name = "Tarun",subject="DSA",language="Python",salary=100000)
dev.details()