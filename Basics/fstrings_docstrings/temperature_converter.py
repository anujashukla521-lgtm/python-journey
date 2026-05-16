# A temperature conversion program that converts Celsius into Fahrenheit using a function and formatted output.

feh = 0
cel = 0
def convertor(temp):
    '''converts celcius to fahrenheit'''
    feh = (9//5*temp)+32
    return feh

celcius = float(input("Enter temperature in celcius: "))
convert = convertor(celcius)
print(f"{celcius} in celcius is {convert} in fahrenheit")
