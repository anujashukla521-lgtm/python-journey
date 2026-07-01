class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        return Complex(
            self.real+other.real,
            self.imag+other.imag
            )

    def __sub__(self,other):
        return Complex(
            self.real-other.real,
            self.imag-other.imag
        )

    def __mul__(self,other):
        real = (self.real*other.real) - (self.imag*other.imag)
        imag = (self.real*self.imag) + (self.imag*self.real)
        return Complex(real,imag)

    def __eq__(self,other):
        return self.real==other.real and self.imag==other.imag

    def __str__(self):
        if self.imag>=0:
            return f"{self.real}+{self.imag}i"
        else:
            return f"{self.real}-{self.imag}i"


c1 = Complex(9,5)
c2 = Complex(7,3)

print("Addition",c1+c2)
print("Subtraction",c1-c2)
print("Multiplication",c1*c2)
print("Equal",c1==c2)