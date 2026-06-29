class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no 

    def __str__(self):
        return f"Student: {self.name} (Roll no: {self.roll_no})"

stu = Student("Anuja Shukla",21)
print(stu)