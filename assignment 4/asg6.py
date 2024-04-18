"""Yash and Vishal have invested 10000$ in their bank. Yash is getting 6% simple 
interest from his bank and Vishal is getting 6% compound interest from his bank. 
Write a python program to calculate the difference in their returns after 30 years. 
What is the difference in their return in one year? What is the reason for this 
difference? Discuss ● Hint: Use the following parameters to calculate interest 
● Principal amount ● Time ● Rate of interest"""

def simple_interest(principle,rate,time):
    interest = (principle * rate * time) / 100
    return principle+interest

def compound_interest(principle,rate,time):

    amount = principle * ( 1 + rate / 100) ** time
    return amount

def main():
    principle = 10000
    rate = 6
    time = 30

    yash_return = simple_interest(principle,rate,time)

    vishal_return = compound_interest(principle,rate,time)

    difference =  vishal_return - yash_return

    print("yash $",yash_return)
    print("vishal $",vishal_return)
    print("Difference in returns after 30 years: ${:.2f}".format(difference))


if __name__ == "__main__":
    main()