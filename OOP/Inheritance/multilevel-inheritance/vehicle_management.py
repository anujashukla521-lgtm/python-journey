class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def vehicle_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type = fuel_type

    def car_info(self):
        print(f"Fuel type: {self.fuel_type}")

class ElectricCar(Car):
    def __init__(self,brand,model,fuel_type,battery_capacity):
        super().__init__(brand,model,fuel_type)
        self.battery_capacity = battery_capacity

    def battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity}")

car = ElectricCar("Toyota",2002,"Petrol","2")
car.vehicle_info()
car.car_info()
car.battery_info()