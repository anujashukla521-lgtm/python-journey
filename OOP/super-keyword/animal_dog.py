class Animal:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def make_sound(self):
        super().make_sound()
        print("Dog barks")


obj1 = Dog("Fluffy")
obj1.make_sound()