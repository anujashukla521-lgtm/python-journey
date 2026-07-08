class Animal:
    def eat(self):
        print("Animals can eat")

class Bird(Animal):
    def fly(self):
        print("Birds can fly")

class Fish(Animal):
    def swim(self):
        print("Fishes can swim")

class Duck(Bird, Fish):
    def qualities(self):
        self.eat()
        self.fly()
        self.swim()

duck = Duck()
duck.qualities()