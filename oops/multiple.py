class A:
    def __init__(self):
        self.a = 100
        self.b = 200

    def m1(self):
        print("This is M1 method")

class B:
    def __init__(self):

        self.x = 101
        self.y = 201

    def m2(self):
        print("This is m2 method")

class C(A,B):

    def __init__(self):
        A.__init__(self)
        B.__init__(self)

        self.m = 1000
        self.n = 2000

    def m3(self):
        print("This is m3 method")


obj = C()
obj.m1()
print(obj.x)
print(obj.a)
obj.m2()
print(obj.y)
print(obj.b)
print(obj.m)
print(obj.n)
obj.m3()




        