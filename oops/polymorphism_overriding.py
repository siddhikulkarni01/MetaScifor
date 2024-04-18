class qcc:
    def __init__(self):
        self.a = 100

    def trainer(self):
        print("good in c programming")

class pyspider(qcc):
    def __init__(self):
        super().__init__()
        self.a = 10

    def trainer(self):
        print("good in python programming")

p1 = pyspider()
q1 = qcc()
print(q1.a)
p1.trainer()
print("attribute of class pyspider",p1.__dict__)