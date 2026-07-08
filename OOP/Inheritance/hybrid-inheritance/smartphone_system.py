class Device:
    def __init__(self,brand,**kwargs):
        self.brand = brand
        super().__init__(**kwargs)

class Camera(Device):
    def take_photo(self):
        print(f"Camera can take photos")

class Phone(Device):
    def calls(self):
        print(f"Phone can make calls")

class SmartPhone(Camera,Phone):
    def browse_internet(self):
        print("Smart phone can browse internet")

obj = SmartPhone("Samsung")
print(obj.brand)
obj.take_photo()
obj.calls()
obj.browse_internet()