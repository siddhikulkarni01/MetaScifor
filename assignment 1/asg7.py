
a = int(input("enter 1st number :"))
b = int(input("enter 2nd number :"))

cases = input("+,-,*,/ ")

match cases:
    case "+":
        print(f"{a} + {b} = {a+b}")
    case "-":
        print(f"{a} - {b} = {a-b}")
    case "*":
        print(f"{a} * {b} = {a*b}")
    case "/":
        print(f"{a} / {b} = {a/b}")
    case _:
        print("invalid input")

