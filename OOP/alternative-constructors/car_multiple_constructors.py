class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    @classmethod
    def from_string(cls,data):
        brand,year = data.split("-")
        return cls(brand,int(year))

    @classmethod
    def from_dict(cls,data):
        brand = data["brand"]
        year = data["year"]
        return cls(brand,int(year))


    def display(self):
        print(f"Brand: {self.brand}\nYear: {self.year}")

c1 = Car("Toyota",2025)
c2 = Car.from_string("Hyundai-2022")
c3 = Car.from_dict({"brand": "Maruti Suzuki","year":2023})

c1.display()
c2.display()
c3.display()