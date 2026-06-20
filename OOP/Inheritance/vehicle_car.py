# A program demonstrating inheritance and protected members (_year), where the Car class inherits common vehicle attributes and adds fuel type information.

class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self._year = year

class Car(Vehicle):
    def __init__(self,brand,year,fuel_type):
        super().__init__(brand,year)
        self.fuel_type = fuel_type

    def display(self):
        print("\n====CAR DETAILS====")
        print(f"Brand: {self.brand}")
        print(f"Year: {self._year}")
        print(f"Fuel type: {self.fuel_type}")


try:
    brand = input("Enter brand: ")
    year = int(input("Enter year: "))
    fuel = input("Enter fuel type: ")

    car1 = Car(brand,year,fuel)
    car1.display()
except ValueError as e:
    print(e)
