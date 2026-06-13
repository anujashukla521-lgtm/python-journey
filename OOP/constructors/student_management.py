class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no 
        if len(marks)!=3:
            raise ValueError("Exactly 3 marks required")
        self.marks = marks
        self.average = 0

    def calculate_average(self):
        total = 0 
        for mark in self.marks:
            total+=mark

        self.average = total/len(self.marks)
        return self.average
        

    def calculate_result(self):
        if self.average>=40:
            return "Pass"
        else:
            return "Fail"

    def display_result(self):
        print(f"Name: {self.name}")
        print(f"Roll no: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average}")
        print(f"Result: {self.calculate_result()}")


obj1 = Student("Harry",1,[78,23,65])
obj1.calculate_average()
obj1.display_result()