a = int(input())
b = int(input())
op = input("+,-,*,/")

match op:
    case "+":
        print(a,op,b,"=",a+b)
    case "-":
        print(a,op,b,"=",a-b)
    case "*":
        print(a,op,b,"=",a*b)
    case "/":
        print(a,op,b,"=",a/b)
    case _:
        print("Invalid input")
            

