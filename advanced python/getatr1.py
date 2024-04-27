def getatr(obj):
    """Returns a list of attributes of an object."""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

class Example:
    def __init__(self):
        self.a = 1
        self.b = "Hello"
        self._c = True  # Protected attribute
        self.__d = [1, 2, 3]  # Private attribute

    def method(self):
        pass

# Create an instance of the Example class
obj = Example()

# Use the getatr() function to get the attributes
attributes = getatr(obj)
print(attributes)  # Output: ['a', 'b', '_c']

print(dir(obj))