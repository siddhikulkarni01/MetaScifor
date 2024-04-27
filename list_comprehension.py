l1 = [1,2,3,4,5]

#list comprehension
squares = [x**2 for x in l1]
print(squares)

#map
def square(x):
    return x**2

squared = map(square,l1)
print("using map",list(squared))


#using filter

def even(x):
    return x % 2 == 0

even_no = filter(even,l1)
print(list(even_no))

#using map and filter  

result = map(lambda x:x**2, filter(lambda x:x%2 == 0,l1))
print(list(result))

#closure
def outer_function(x):
    def inner_func(y):
        return x+y
    return inner_func

first = outer_function(10)
second = first(20)
print(second)