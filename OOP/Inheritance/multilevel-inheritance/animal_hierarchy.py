class Animal:
    def eat(self):
        print("Animal can eat")

class Mammal(Animal):
    def walk(self):
        print("Mammals can walk")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()