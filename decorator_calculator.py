def calculator(function):
    def wrapper(*args):

        while True:
            try:
                num1 = int(input("enter the 1st no. "))
                num2 = int(input("enter 2nd no. "))
                res = function(num1,num2,*args)
                print("Result :",res)
            except ValueError:
                print("please enter valid number")
            
            choice = input("Do u want to continue calculator(yes/no)").lower()

            if choice != "yes":
                break
    return wrapper
    

@calculator
def add(num1,num2):
    return num1 + num2

@calculator
def sub(num1,num2):
    return num1 - num2

@calculator
def mul(num1,num2):
    return num1 * num2

@calculator
def div(num1,num2):
    return num1/num2

add()
sub()
mul()
div()

