class Temperature:
    def __init__(self,temp):
        self.temperature = temp

    @property
    def temperature(self):
        return self._temp

    @temperature.setter
    def temperature(self,value):
        if value<-273.15:
            raise ValueError("Temperature cannot be below absolute zero")

        self._temp = value

    @property
    def fahrenheit(self):
        return (self._temp*1.8)+32

celcius = float(input("Enter temperature in celcius: "))
obj1 = Temperature(celcius)
print("Celcius:", obj1.temperature)
print("Fahrenheit:", obj1.fahrenheit)