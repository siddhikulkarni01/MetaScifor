"""Scarlet, a fifteen year old, wants to be creative and is inspired by watching
alexa, siri, google on how they act as smart chatbots and assistants and wanted 
to create her own chatbot. So write a program in python using the if-else, Nested 
if-else, if-else-if ladder where ever necessary.
The Bot Has the Behave in following manner
Step 1: ask the user for his/her name.
Step 2: wish the user by telling his name For Ex: Hi My name is Jenni, chatbot.
 A Very Good Day To You username!!.
Step 3: How are you feeling today??(Based on what user entered you are suppose to 
respond if user entered good statement then say something positive like."It's really 
a productive day to do something innovative and you are close to it. "If the user 
says something negative then respond accordingly and try to cheer him up."""

def greet_user():
    name = input("Step 1: Hi there! what's your name ")
    print("Step 2: Hi, My name is Scarlet, your chatbot. A Very Good Day To You, {}!!".format(name))
    return name 

def respond_to_feeling():
    feeling = input("How are you feeling Today!")

    if "good" in feeling.lower():
        print("It's really a productive day to do something innovative and you are close to it.")
    elif "bad" in feeling.lower() or "not good" in feeling.lower() or "sad" in feeling.lower():
        print("I'm sorry to hear that. Remember, tough times don't last, but tough people do. You've got this!")
    else:
        print("I understand. We all have our ups and downs. Just remember, every day is a new opportunity.")

greet_user()
respond_to_feeling()