"""Shubham had created a BMI calculator to check his health condition daily. But he is not able to record the
values. He wants to see how his BMI is changing. So he decided to connect his BMI program with a text file 
using the concept of file handling. Now, when he uses his BMI program, his height, weight, BMI, and date get 
added to a text file "bmi.txt". Create a program that can do the same thing for you."""
import datetime

def calculate_bmi(weight,height,):

    return  (weight / height ** 2) * 703

    
def record_bmi(weight,height):

    bmi = calculate_bmi(weight,height)
    name = ''.join(input("enter your name").split())
    current_time = datetime.datetime.now()


    with open('bmi.txt','a') as file:
        file.write(f"Name : {name}\t")
        file.write(f"weight : {weight}\t")
        file.write(f"height : {height}\t")
        file.write(f"BMI : {bmi}\t")
        file.write(f"current time : {current_time} \n")

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    record_bmi(weight, height)
    print("BMI record has been saved.")

if __name__ == "__main__":
    main()
