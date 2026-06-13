class Car:
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_details(self):
        print("======CAR DETAILS======\n")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")



car_brand = input("Enter brand: ")
car_model = input("Enter model: ")
car_year = int(input("Enter year: "))
car1 = Car(car_brand,car_model,car_year)
car1.show_details()