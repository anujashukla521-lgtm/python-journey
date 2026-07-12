class Wifi:
    def connect_wifi(self):
        print("Wifi connected")

class Bluetooth:
    def connect_bluetooth(self):
        print("Bluetooth connected")

class Camera:
    def open_camera(self):
        print("Camera opened")

class SmartPhone(Wifi,Bluetooth,Camera):
    def start_device(self):
        self.connect_wifi()
        self.connect_bluetooth()
        self.open_camera()
        print("Device ready")

phone = SmartPhone()
phone.start_device()