class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no 

class ProgrammingStudent(Student):
    def __init__(self,name,roll_no,language,marks):
        super().__init__(name,roll_no)
        self.language = language
        self.marks = marks

    def isPass(self):
        if self.marks>=40:
            return "Passed"
        else:
            return "Failed"

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll no: {self.roll_no}")
        print(f"Language: {self.language}")
        print(f"Marks: {self.marks}")
        print(f"Result: {self.isPass()}")


stu = ProgrammingStudent("Anuja Shukla",21,"Python",100)
stu.display_details()