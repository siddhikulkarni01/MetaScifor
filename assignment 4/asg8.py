"""8:Shubham is worried about his health. He keeps checking his height and weight
daily. Recently he came to know about the BMI report, and now he wants to calculate
his own BMI by writing a python program. Write a program in python to check your 
BMI by putting your height and weight as input. ● Note: ● Body Mass Index is a 
simple calculation using a person's height and weight. The formula is BMI = kg/m2 
where kg is a person's weight in kilograms and m2 is their height in meters squared. 
A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. BMI 
applies to most adults 18-65 years."""

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
        else:
            bmi = calculate_bmi(weight, height)
            print("Your BMI is:", bmi)
            if bmi < 18.5:
                print("BMI Category: Underweight")
            elif 18.5 <= bmi <= 24.9:
                print("BMI Category: Normal weight")
            else:
                print("BMI Category: Overweight")
    except ValueError:
        print("Invalid input. Please enter valid weight and height.")

if __name__ == "__main__":
    main()
