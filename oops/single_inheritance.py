class base:

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def display(self):

        print(f"Hi my name is {self.name} and my age is {self.age}")

class derived(base):

    def __init__(self,name,age,address):

        super().__init__(name,age)
        self.address = address
        

    def disp(self):
        print(f"from derived class name is {self.name} age is {self.age}")

obj = base("sid","24")
obj.display()

o1 = derived("siddhi","27","bangalore")
o1.disp()
o1.display()


        
