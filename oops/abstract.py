from abc import ABC,abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimter(self):
        pass

class Rectangle(Shape):

    def __init__(self,length,breadth):

        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length * self.breadth)   

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        return 3.14 * self.radius**2
    
    def perimeter(self):
        return 2 * 3.1 * self.radius

rect = Rectangle(5,10)

cir = Circle(7)

print("Area of rectangle:", rect.area()) 
print("Perimeter of rectangle:", rect.perimeter()) 
print("Area of circle:", cir.area())      
print("Perimeter of circle:", cir.perimeter()) 
