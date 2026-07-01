class Fraction:
    def __init__(self,num,den):
        if den == 0:
            raise ValueError("Denominator can't be zero")
            
        self.num = num
        self.den = den 

    def __add__(self,other):
        numerator = (self.num * other.den) + (other.num * self.den)
        denominator = self.den * other.den
        return Fraction(numerator , denominator)

    def __str__(self):
        return f"{self.num} / {self.den}"

try:

    f1 = Fraction(1,2)
    f2 = Fraction(3,4)

    print(f1 + f2)
except ValueError as e:
    print(e)