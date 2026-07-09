class Appliance:
    def turn_on(self):
        print("Turn on the appliance")

class WashingMachine(Appliance):
    def wash(self):
        self.turn_on()
        print("Washing machine washes clothes")

class Refrigerator(Appliance):
    def cool(self):
        self.turn_on()
        print("Refrigertor cools the edibles")

class Microwave(Appliance):
    def heat(self):
        self.turn_on()
        print("Microwave heats the edibles")

obj1 = WashingMachine()
obj2 = Refrigerator()
obj3 = Microwave()

obj1.wash()
obj2.cool()
obj3.heat()