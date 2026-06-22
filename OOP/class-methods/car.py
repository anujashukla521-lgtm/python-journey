# A Python program implementing an alternative constructor with a class method to create car objects with predefined default values.

class Car:
    total_cars = 0
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
        Car.total_cars +=1

    def display_details(self):
        print(f"Brand: {self.brand}\nYear: {self.year}")

    @classmethod
    def create_default_car(cls):
        return cls("Toyota",2025)

car1 = Car.create_default_car()
car1.display_details()
