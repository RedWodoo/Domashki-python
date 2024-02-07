class Complex:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        znam = other.real ** 2 + other.imag ** 2
        return Complex((self.real * other.real + self.imag * other.imag) / znam,
                       (self.imag * other.real - self.real * other.imag) / znam)

    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

x = Complex(1, 1)
y = Complex(2, 2)
z = Complex(3.14)

res1 = x + y
res2 = x * y
res3 = x
res4 = y
x *= y


if x == y:
    print(x, "=", y)
else:
    print(x, "!=", y)


c = z.magnitude()
print("double(res1):", c)



