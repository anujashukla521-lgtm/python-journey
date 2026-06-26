class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    @classmethod
    def from_string(cls,data):
        name,age,marks = data.split("-")
        return cls(name,int(age),float(marks))

    def display_details(self):
        print(f"Name: {self.name}\nAge: {self.age}\nMarks: {self.marks}")

    def grade(self):
        if self.marks>=90:
            print ("Grade: A")
        elif self.marks>=80:
            print ("Grade: B")
        elif self.marks>=70:
            print ("Grade: C")
        else:
            print ("Grade: D")

stu1 = Student("Gargi",19,98)
stu2 = Student.from_string("Harshita-20-81")

stu1.display_details()
stu1.grade()
stu2.display_details()
stu2.grade()