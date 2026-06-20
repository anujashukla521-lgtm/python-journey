# A Python program demonstrating encapsulation using private attributes, getters, setters, and @property decorators to manage and validate student marks.

class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no 
        self.marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,value):
        if value<0 or value>100:
            raise ValueError("Marks must be between 0 and 100")

        self.__marks = value

    def show(self):
        print(f"Name: {self.name}")
        print(f"Roll no: {self.roll_no}")
        print(f"Marks: {self.marks}")

try:
    name = input("Enter name: ")
    roll = int(input("Enter roll no: "))
    marks = float(input("Enter marks: "))
    s1 = Student(name,roll,marks)
    s1.show()
except ValueError as e:
    print(e)
