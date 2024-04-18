class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Creating instances
dog = Dog()
cat = Cat()

# Accessing methods
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks

cat.speak()  # Output: Animal speaks
cat.meow()   # Output: Cat meows
