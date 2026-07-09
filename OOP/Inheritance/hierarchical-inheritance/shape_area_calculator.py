class Shape:
    def __init__(self,color):
        self.color = color

class Circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,color,length,width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

class Triangle(Shape):
    def __init__(self,color,base,height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        return 1/2*(self.base*self.height)

circle = Circle("Red",2)
rect = Rectangle("Yellow",4,5)
tri = Triangle("Orange",7,1)

print("Area of cirlce:",circle.area())
print("Area of rectangle:",rect.area())
print("Area of triangle:",tri.area())