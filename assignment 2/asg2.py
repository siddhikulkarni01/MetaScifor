"""It's Domino's 25th Anniversary and is planning for a big give away and in order to choose the lucky draw 
winner Domino's first needs to collect all of its customer details. On collecting the customer details
 Domino's even wants to thank each and every customer for visiting as soon as they entered their details.
 Write a program to accept customer details like customer name, customer mobile number, customer age,
customer email Id.On successfully receiving all the customer information write a print() to thank the
customer by using his name for example"Hi", customerName,"!! Thanks for visiting our restaurant and 
registering for our lucky draw competition on our 25th Anniversary.""Once the lucky draw results are 
announced you will receive a message on your mobile number :",customerMobileNumber"An detailed description
of your gift on your email Id :",customerEmailId"Thank you for being a valued customer",customerName,"!!""Dominos"
"""

import re

print("Dear customer, kindly Enter the data for lucky draw !!!")

def customer_details(name, mobile, age, email):
    if name is not None and len(str(mobile)) == 10 and age > 0 and re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return name, mobile, age, email
    else:
        return None

name = input("Enter your name: ")
mobile = input("Enter your mobile number: ")
age = input("Enter your age: ")
email = input("Enter your email id: ")

details = customer_details(name, mobile, int(age), email)
if details is not None:
    print(f"""Hi", {name},"!! Thanks for visiting our restaurant and 
registering for our lucky draw competition on our 25th Anniversary.""Once the lucky draw results are 
announced you will receive a message on your mobile number :{mobile} .An detailed description
of your gift on your email Id :"{email}"Thank you for being a valued customer",{name}"!!""Dominos"
""")
    
else:
    print("Invalid input. Please provide valid details.")




