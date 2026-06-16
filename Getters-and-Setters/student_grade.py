# A Python OOP program that validates student grades using getters and setters and calculates letter grades automatically through a computed property.

class Student:
    def __init__(self, name, grade):
        self._name = name
        self.grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,value):
        if 0<=value<=100:
            self._grade = value
        else:
            raise ValueError("Grade must be between 0 and 100")


    @property
    def letter_grade(self):
        if self._grade>=90:
            return "A"
        elif self._grade>=80:
            return "B"
        elif self._grade>=70:
            return "C"
        elif self._grade>=60:
            return "D"
        else:
            return "F"


name = input("Enter name: ")
grade = int(input("Enter grade: "))
try:

    s = Student(name,grade)
    print("Name:",s._name)
    print("Grade:",s._grade)
    print("Letter grade:",s.letter_grade)
except ValueError as e:
    print(e)
