"""Aarush recently learned probability in his school. He was finding the probability 
of different events and he wondered whether he can develop a program to do the same 
thing or not. To help Aarush create a program in python where user can enter number
of favorable outcomes and total number of possible outcomes and then program will 
print the probability of that event on the screen. ● Note: ● Print the probability
of the event only up to 2 decimal places. ( For this use round() function ) 
● Sample run ● >>Enter the number of favorable outcomes: 1
● >>Enter the total number of possible outcomes: 2 ● >>Probability: 0.5"""

def calculate_probability(favourable_outcomes,total_outcomes):
    probability = favourable_outcomes / total_outcomes
    return round(probability,2)

favourable_outcomes = int(input())
total_outcomes = int(input())

print(calculate_probability(favourable_outcomes,total_outcomes))