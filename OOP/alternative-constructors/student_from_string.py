class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")


    @classmethod
    def from_string(cls,data):
        name,age = data.split("-")
        return cls(name,int(age))

stu = Student.from_string("Anuja-100")
stu.display()