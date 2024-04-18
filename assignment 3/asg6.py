"""Bonnie visited the amusement park with her father. She enjoyed all the rides very much but one in particular
 caught her eye. The one and only rollercoaster!BUT! There is a age requirement for riding that coaster. 
 The minimum age required is 10. If Bonnie is 15 years old, can we check if she can ride the rollercoaster?"""

age = int(input())

if age < 0:
    print("Invalid input ")
elif age < 10:
    print("you are not eligible for rollercoster ride")
else:
    print("you are eligible to ride rollercoaster ")