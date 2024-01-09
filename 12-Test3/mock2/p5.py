import math

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        elif self.x == 0 and self.y != 0:
            return 0  # On Y-axis
        elif self.x != 0 and self.y == 0:
            return 0  # On X-axis
        else:
            return 0  # Origin (0,0)

    def m2(self, a, b):
        return self.m1() == C(a, b).m1()

    def m3(self, a, b):
        distance = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        return distance > 5

p = C(2, 3)
print(p.m1())
print(p.m2(7, 4))
print(p.m2(-3, 1))
print(p.m3(8, 5))
print(p.m3(4, 7))

p1 = C(0, 5)
print(p1.m1())
print(p1.m2(4, 7))
print(p1.m2(-7, 0))