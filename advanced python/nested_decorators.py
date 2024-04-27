def inner_decorator(function):
    def wrapper(*args,**kwargs):
        res = function(*args,**kwargs)
        print("inner decorator")
        return res
    return wrapper


def out_decorator(function):
    @inner_decorator
    def inner_wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        print("outer decorator")
        return res 
    return inner_wrapper

@out_decorator
def result():
    return "example"

print(result())
