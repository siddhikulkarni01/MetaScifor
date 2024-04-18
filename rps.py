import random


def guess(input_string):
    x = ['rock','paper','scissor']
    choice =  random.choice(x)

    if input_string in x:
        if input_string == choice:
            return "its a tie"
        elif input_string == "rock" and choice == "paper":
            return "you lose"
        elif input_string == "rock" and choice == "scissor":
            return "you win"
        elif input_string == "paper" and choice == "scissor":
            return "you lose"
        elif input_string == "paper" and choice == "rock":
            return "you win"
        elif input_string == "scissor" and choice == "paper":
            return "you win"
        elif input_string == "scissor" and choice == "rock":
            return "you lose"
        
    else:
        print("Invalid input")

input_String = input()
print(guess(input_String))


