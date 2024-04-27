def uppercase(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)

        return res.upper()
    return wrapper

class A:
    def method_a(self,a,b):
        print("method a")
        return a * b

      
    
class B:
    def method_b(self,a,b):
        print("method b")
        return a + b
       
    
class C(A,B):
    def method_c(self,a,b,c):
        print("method 3")
        return a * b - c
 
        

obj = C()

print(obj.method_a(2,4))
print(obj.method_b(2,1))
print(obj.method_c(2,6,1))