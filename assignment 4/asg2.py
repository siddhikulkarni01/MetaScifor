"""The RTO (Regional Transport Office) website holds a registration form which is 
responsible for registering a user for a Driving License. The RTO wants to take the 
next step if and only if the user's age is greater than or equal to 18.
So write a program in python to help the RTO find out whether the registered user's 
age is greater than or equal to 18 or not."""

def user_data():

    print("enter your name")
    name = input("Name :")

    print("enter your age")
    age = int(input("Age :"))

    if age >= 18:
        print(f"Hi {name} you are eligible to apply for driving license")
    else:
        print(f"dear {name} you are not eligible to apply for driving license")


user_data()


