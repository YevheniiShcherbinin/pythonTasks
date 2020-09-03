class Triangle(object):
    def __init__(self):
        pass

    def area(self, a, b, c):
        w = (self.a + self.b + self.c) // 2
        return (w * (w - self.a) * (w - self.b) * (w - self.c)) ** 0.5

    def perimeter(self, a, b, c):
        return (self.a + self.b + self.c)

    def kind(self, a, b, c):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return print("Triangle not exist")
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return print("Versatile")
        elif self.a * self.a + self.b * self.b == self.c * self.c:
            return print("Rectangular")
        elif self.a == self.b == self.c:
            return print("Equilateral")
        else:
            return print("Isosceles")


#a = int()
#b = int()
#c = int()
#print("Area =", area.Triangle())
#print("Perimeter =", perimeter.Triangle)
#print("Kind =", kind.Triangle())

