"""Himanshu sells notebooks. Sometimes it becomes a bit difficult for him to
 calculate the total amount to charge from the customer. To help Himanshu create
 a program that asks the user to enter the number of books to buy and then print 
 the amount to be paid. ● Hint: Assume the cost of one notebook - $2"""

def calculate(quantity):
    price = 2
    
    total = quantity*price

    return total

q = int(input("enter the quantity "))

print("Total price is",calculate(q),"$")
