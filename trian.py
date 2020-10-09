
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        w = (self.a + self.b + self.c) // 2
        e = (w * (w - self.a) * (w - self.b) * (w - self.c)) ** 0.5
        return e

    def perimeter(self):
        r = (self.a + self.b + self.c)
        return r

    def kind(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "Triangle not exist"
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return "Versatile"
        elif self.a * self.a + self.b * self.b == self.c * self.c:
            return "Rectangular"
        elif self.a == self.b == self.c:
            return "Equilateral"
        else:
            return "Isosceles"


tri1 = Triangle(3, 4, 5)
print("Area =",  tri1.area())
print("Perimeter =", tri1.perimeter())
print("Kind =", tri1.kind())



