class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    @classmethod
    def from_string(cls,data):
        length,width = data.split("X")
        return cls(float(length),float(width))

    def area(self):
        print(f"Area: {self.length*self.width}")

    def perimeter(self):
        print(f"Perimeter: {2*(self.length+self.width)}")


rec1 = Rectangle.from_string("10X20")
rec1.area()
rec1.perimeter()