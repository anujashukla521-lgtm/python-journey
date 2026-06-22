# A Python program demonstrating an alternative constructor using a class method to create Student objects from a formatted string.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls,data):
        name, age = data.split('-')
        return cls(name,int(age))


stu = Student.from_string("Anuja-100")
print(stu.name)
print(stu.age)
