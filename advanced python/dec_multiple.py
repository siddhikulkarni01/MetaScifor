def result(func):
    def wrapper(*args):
        res = func(*args)
        return res.upper() * 2
    return wrapper

def ex(func1):
    def inside_wrapper(*args1):
        res = func1(*args1) + '! '
        return res
    return inside_wrapper



# @ex
@result
@ex
def abc():
    return "Hello world "

print(abc())