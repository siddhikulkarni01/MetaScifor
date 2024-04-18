bank_balance =  5000

def withdraw(amount):

    global bank_balance

    if amount % 100 != 0:
        print("Amount should be multiple of 100")
    elif amount > bank_balance:
        print("Insufficient balance")
    else:
        bank_balance -= amount
        print (f"Withdraw succesfull , available balance is {bank_balance}")

def enquiry():
    print("Available balance is ",bank_balance)

def deposit(amount):

    global bank_balance

    bank_balance += amount

    print(f"Amount deposit successfull, new balance is {bank_balance}")

def fast_cash(option):

    global bank_balance
    options = [5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000]

    if option not in options:
        print("Invalid option ")
    elif option > bank_balance:
        print("Insufficient Fund ")
    else:
        bank_balance -= option
        print(f"Withdraw successful, available balance",bank_balance)

def main():

    while True:
        print("\n Atm main menu")
        print("1. Withdraw :")
        print("2. Deposit :")
        print("3. Balance Enquiry :")
        print("4. Fast cash :")
        print("5. Exit")

        choice = int(input())

        if choice == 1:
            print("withdraw")
            amount = int(input("Enter amount"))
            withdraw(amount)
        elif choice == 2:
            print("deposit")
            amount = int(input("Deposit amount"))
            deposit(amount)
        elif choice == 3:
            print("balance enquiry")
            enquiry()
        elif choice == 4:
            print("Fast Cash Options: 5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000")
            option = int(input("Select an option: "))
            fast_cash(option)
        elif choice == 5:
            print("Thank you for using our ATM")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()





    