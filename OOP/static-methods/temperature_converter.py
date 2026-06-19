class TemperatureConvertor:

    @staticmethod
    def celcius_to_fahrenheit(celcius):
        return (celcius*1.8)+32

    @staticmethod
    def fahrenheit_to_celcius(fahrenheit):
        return (fahrenheit-32)*1.8

    @staticmethod
    def celcius_to_kelvin(celcius):
        return celcius+273.15


print("Celcius to fahrenheit:",TemperatureConvertor.celcius_to_fahrenheit(25))
print("Fahrenheit to celcius:",TemperatureConvertor.fahrenheit_to_celcius(12))
print("Celcius to kelvin:",TemperatureConvertor.celcius_to_kelvin(12))