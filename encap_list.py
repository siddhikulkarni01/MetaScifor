class mylist:
    def __init__(self, data):
        self._data = data 

    def append(self, item):
        self._data.append(item)

    def extend(self, items):
        self._data.extend(items)

    def pop(self):
        return self._data.pop()
    
    def remove(self, item):
        self._data.remove(item)

    def reverse(self):
        self._data.reverse()

    def __str__(self):
        return str(self._data)
    
my_list = mylist([1, 2, 3, 4])
print("initial list:", my_list)

my_list.append(5)
print("after appending 5:", my_list)

my_list.extend([7, 8, 9])
print("after extending :", my_list)

my_list.pop()
print("after popping last element from the list:", my_list)

my_list.remove(5)
print("after removing 5:", my_list)

my_list.reverse()
print("after reversing",my_list)

