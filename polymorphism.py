class Dog:

    def breed(self):
        print("its a lab")

    def noise(self):
        print("bark")

class Cat:

    def breed(self):
        print("percian cat")

    def noise(self):
        print("meow")

def animal(obj):

    obj.breed()
    obj.noise()

d1=Dog()
c1=Cat()

d1.breed()
d1.noise()
c1.breed()
c1.noise()