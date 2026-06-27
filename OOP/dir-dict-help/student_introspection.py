class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")


student = Student("Anuja Shukla", 100, 99.9)
student.display()
print(student.__dict__)
print(dir(student))
help(Student)