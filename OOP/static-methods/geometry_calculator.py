class GeometryCalculator:

    @staticmethod
    def area_of_square(side):
        return side*side

    @staticmethod
    def area_of_rectangle(length,width):
        return length*width

    @staticmethod
    def area_of_circle(radius):
        return 3.14159*radius*radius

print("Area of square:",GeometryCalculator.area_of_square(5))
print("Area of rectangle:",GeometryCalculator.area_of_rectangle(4,2))
print("Area of circle:",GeometryCalculator.area_of_circle(3))