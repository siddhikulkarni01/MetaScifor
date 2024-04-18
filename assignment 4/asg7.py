"""Nidhi's father is not able to calculate his annual tax correctly. He is a bit 
confused with the taxation rule also each year his total annual income is different.
 So to help her father Nidhi decides to write a python program that can calculate 
 the tax to be paid based on annual income. Write the same program to calculate the 
 tax to be paid based on annual income. ● Hint: take the annual income as input from 
 the user and print the amount of tax to be paid. These are tax rules."""
def calculate_tax(annual_income):
    tax = 0
    if annual_income <= 250000:
        tax = 0
    elif 250001 <= annual_income <= 500000:
        tax = (annual_income - 250000) * 0.05
    elif 500001 <= annual_income <= 1000000:
        tax = 25000 + (annual_income - 500000) * 0.2
    else:
        tax = 125000 + (annual_income - 1000000) * 0.3
    return tax

def main():
    try:
        annual_income = float(input("Enter your annual income: "))
        if annual_income < 0:
            print("Annual income cannot be negative.")
        else:
            tax = calculate_tax(annual_income)
            print("Tax to be paid: ${:.2f}".format(tax))
    except ValueError:
        print("Invalid input. Please enter a valid annual income.")

if __name__ == "__main__":
    main()
