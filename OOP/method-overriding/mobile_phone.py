class Mobile:
    def features(self):
        print("Calling")
        print("Messaging")

class SmartPhone(Mobile):
    def features(self):
        super().features()
        print("Internet")
        print("Camera")
        print("Face unlock")

obj = SmartPhone()
obj.features()