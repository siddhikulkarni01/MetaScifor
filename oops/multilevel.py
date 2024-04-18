class one:
    def __init__(self):
        self.a = 100
        self.b = 200
    
class two(one):
    def __init__(self):
        super().__init__()
        self.x = 1000
        self.y= 2000

class three(two):
    def __init__(self):
        super().__init__()
        self.m = 101
        self.n = 201

o1 = one()
print("attribute of class one ->",o1.__dict__)
print()
o2 = two()
print("attribute of class two ->",o2.__dict__)
print()
o3=three()
print("attributes of class three ->",o3.__dict__)