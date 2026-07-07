class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_student(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class CollegeStudent(Student):
    def __init__(self,name,age,college):
        super().__init__(name,age)
        self.college = college

    def display_college(self):
        print(f"Collge: {self.college}")

class EngineeringStudent(CollegeStudent):
    def __init__(self,name,age,college,branch):
        super().__init__(name,age,college)
        self.branch = branch

    def display_branch(self):
        print(f"Branch: {self.branch}")

obj = EngineeringStudent("Gagan",21,"ABC","BTech")
obj.display_student()
obj.display_college()
obj.display_branch()