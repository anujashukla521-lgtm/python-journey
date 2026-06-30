class Shape:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"Shape name: {self.name}")

class Circle(Shape):
    def __init__(self,name):
        super().__init__(name)

    def display(self):
        super().display()
        print("This is a circle")

obj = Circle("Circle")
obj.display()