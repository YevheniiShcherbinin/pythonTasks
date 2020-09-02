class Triangle(object):
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def area(self):
        w = (self.a + self.b + self.c) // 2
        k = (w * (w - self.a) * (w - self.b) * (w - self.c)) ** 0.5
        return k

    def perimeter(self):
        q = (self.a + self.b + self.c)
        return q

    def kind(self):
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


a = int(input())
b = int(input())
c = int(input())
q = Triangle(a, b, c)
w = Triangle(a, b, c)
k = Triangle(a, b, c)
