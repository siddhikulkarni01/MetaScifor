from datetime import datetime

def calculate_age(year_of_birth,month_of_birth):

    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month

    age_in_year = current_year - year_of_birth
    if current_month < month_of_birth:
        age_in_year -= 1
        months = 12 - (month_of_birth- current_month)
    else:
        months = current_month - month_of_birth
    
    return age_in_year,months

year_of_birth =  int(input("enter year of birth :"))
month_of_birth =  int(input("enter month of birth :"))

age_year, age_month = calculate_age(year_of_birth,month_of_birth)

print(f"Your age is:", age_year, "years and", age_month, "months.")
