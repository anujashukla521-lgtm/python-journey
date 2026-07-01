class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

    def __gt__(self,other):
        return self.area()>other.area()

    def __lt__(self,other):
        return self.area()<other.area()

    # def __eq__(self,other):
    #     return self.area()==other.area()

rec1 = Rectangle(8,5)
rec2 = Rectangle(8,5)

print("Area of rectangle 1:",rec1.area())
print("Area of rectangle 2:",rec2.area())

if rec1 > rec2:
    print("Rectangle 1 area is greater")
elif rec1 < rec2:
    print("Rectangle 2 area if greater")
else:
    print("Both rectangles have equal area")