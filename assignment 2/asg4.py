def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))


celsius = fahrenheit_to_celsius(fahrenheit)


print("Temperature in Celsius:", celsius)
