# A constructor inheritance example using super() where the Student class extends the Person class by adding course details.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    stu1 = Student(name,age,course)
    stu1.show_details()
except ValueError as e:
    print(e)
