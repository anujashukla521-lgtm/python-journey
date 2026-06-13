class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width

    def calculate_perimeter(self):
        return 2*(self.length+self.width)


length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rec1 = Rectangle(length,width)
print("Area",rec1.calculate_area())
print("Perimtere",rec1.calculate_perimeter())

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rec2 = Rectangle(length,width)
print("Area",rec1.calculate_area())
print("Perimtere",rec1.calculate_perimeter())
