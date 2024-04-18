class Dog:
    def breed(self):
        print("its a lab")
    
    def noise(self):
        print("Bark")

class Cat:
    def breed(self):
        print("its a persian cat")

    def noise(self):
        print("meow")

def animal(obj):
    obj.breed()
    obj.noise()

d1 = Dog()
c1 = Cat()

c1.breed()
c1.noise()
d1.breed()
d1.noise()