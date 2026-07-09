class Vehicle:
    def __init__(self,brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self,brand):
        super().__init__(brand)

    def start(self):
        print(f"Car of brand {self.brand} starts")

class Bike(Vehicle):
    def __init__(self,brand):
        super().__init__(brand)

    def start(self):
        print(f"Bike of brand {self.brand} starts")

class Truck(Vehicle):
    def __init__(self,brand):
        super().__init__(brand)

    def start(self):
        print(f"Truck of brand {self.brand} starts")

car =  Car("Maruti Suzuki")
bike = Bike("Royal Enfield")
truck = Truck("Tata")

car.start()
bike.start()
truck.start()