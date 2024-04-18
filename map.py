# def add(x):
#     return x**2

n = [1,2,3,4,5]

squared_number= map(lambda x:x**2,n)
print(list(squared_number))

filter1 = filter(lambda x: x%2 == 1,n)
print(list(filter1))


# use map and filter together 

n1 = [1,2,3,4,5,6,7,8,9,10]

number = map( lambda x : x**2 , filter(lambda x:x%2 == 0,n1 ))
print(list(number))