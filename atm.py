
balance = 10000


def withdraw(amount):

    global balance

    if amount % 100 != 0:
        print("Enter amount in multiple of 100 only")
    elif amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print("withdraw successfull ! current amount is",balance)

def deposit(amount):

    global balance

    balance += amount

    print("Amount deposited , current balance is ",balance)

def balance_enquiry():

    global balance

    print("Current balance is",balance)


while True:
    
    choice = int(input(f"Enter a choice \n 1.withdraw \n 2.deposit \n 3.balance enquiry \n 4.exit \n"))
    if choice == 1:
        amount = int(input("enter the amount "))
        withdraw(amount)
    elif choice == 2:
        amount = int(input("enter the amount "))
        deposit(amount)
    elif choice == 3:
        balance_enquiry()
    elif choice == 4:
        print("Thankyou for using our atm. please visit again")
        break
    else:
        print("Invalid input")
        break
