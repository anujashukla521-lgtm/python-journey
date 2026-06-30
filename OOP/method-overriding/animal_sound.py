class Animal:
    def sound(self):
        print("Animal makes different sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()