a = 5
print(hash(a))

s = "Ildar"
print(hash(s))

names = ['Ildar', 'Bekaidar', 'Zhandos', 'Dulat']
for name in names:
    print(hash(name))

class C:
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.x)

c1 = C('Ildar')
c2 = C('Ildar')
c3 = C('Dulat')
print(hash(c1))
print(hash(c1))
print(hash(c2))
print(hash(c3))