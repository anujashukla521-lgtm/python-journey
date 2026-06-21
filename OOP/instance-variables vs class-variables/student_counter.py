# A Python program demonstrating the use of class variables and instance variables by tracking the total number of student.

class Student:
    total_students = 0
    def __init__(self,name):
        self.name = name
        Student.total_students+=1

    def display(self):
        print("Name:",self.name,)
        

s1 = Student("Harry")
s2 = Student("Ron")
s3 = Student("Hermoine")

s1.display()
s2.display()
s3.display()
print("Total students:",Student.total_students)

