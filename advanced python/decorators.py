def result(function):
    def wrapper(*args):
        res = function(*args)    
        print(res)
    return wrapper

@result
def hello():
    return "hiiieee"

@result
def add(a,b):
    return a+b

@result
def mul(a,b,c):
    return a*b*c

@result
def sub(a,b,c,d):
    return a-b-c-d

add(2,3)
mul(3,8,2)
sub(100,10,10,10)
hello()

