class C:
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self, s, n):
        self.sectors[s] = n
        
    def m2(self, s):
        total_fans = 0
        for sector in s:
            if sector in self.sectors:
                total_fans += self.sectors[sector]
        return total_fans

stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})

stadium.m1("G", 130)

result1 = stadium.m2("GD")
result2 = stadium.m2("KEJ")

print(result1)  
print(result2)  
