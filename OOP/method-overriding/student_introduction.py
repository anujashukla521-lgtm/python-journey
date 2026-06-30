class Person:
    def introduce(self):
        print("Hello, I am a person")

class Student(Person):
    def introduce(self):
        print("Hello, I am a student")

stu = Student()
stu.introduce()