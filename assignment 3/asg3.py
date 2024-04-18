def is_valid_phone_number(phone_number):
    
    if len(phone_number) == 10 and phone_number.isnumeric():
   
        first_digit = int(phone_number[0])
        if first_digit in [9, 8, 7]:
            return True
    return False


phone_number = input("Enter your phone number: ")

if is_valid_phone_number(phone_number):
    print("Valid phone number!")
else:
    print("Invalid phone number! Please enter a 10-digit number starting with 9, 8, or 7.")
