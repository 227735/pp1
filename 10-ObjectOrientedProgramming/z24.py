class C():
    def __init__(self,coordinates):
        self.coordinates = coordinates

    def m(self,n):
        ilosc = 0
        for x,y in self.coordinates:
            if x > 0 and y > 0:
               ilosc += 1
        return ilosc >= n


c1 = C([[2, 3], [1, 8], [-6, 4], [3, -7]])

result1 = c1.m(2)
result2 = c1.m(3)

print(result1) 
print(result2) 