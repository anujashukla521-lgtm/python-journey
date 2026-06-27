class Calculator:
    def square(self,x):
        return x*x

calc = Calculator()
result = calc.square(4)
print(result)
print(dir(calc))
help(Calculator)