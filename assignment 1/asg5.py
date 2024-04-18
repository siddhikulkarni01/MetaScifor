"""A teacher told students to write an essay on themselves. Nidhi created a python 
program that can generate an essay just by taking inputs. She shared the program with
her friends to help them. Write a python program that can take inputs like name, 
age, address, etc, and convert it into an essay. ● Rakshita wants to create a simple 
chatbot using python language. Write a program in python to help Rakshita in creating
 the chatbot. ● Hint: with the help of variables store the answers of the user and 
 use it for further conversation by the chatbot. 
● Example : ● >> ● Hi, I am a chatbot. What is your name? ● >>Nidhi 
● Oh, Nidhi in which grade you are right now? ● >>8
● Nidhi you are in 8th grade. Can I ask you one question? yes or no? ● >>yes 
● Tell me 1024+98=? ● >>1122 ● Good! Your answer is correct. Bye ● >>bye"""

def chatbot():

    print("Hi i am a chatbot whats your name")
    name = input("<<")

    print(f"oh {name} in which grade you are in")
    grade = input()

    print(f"{name} you are in {grade}th grade. can i ask you a question (yes or no)")
    answer = input()

    if answer == "yes":
        print("Tell me 1024+98=?")
        ans = int(input())

        if ans == 1122:
            print("Good! Your answer is correct. Bye")
        else:
            print("Wrong answer.bye")

    else:
        print("no problem")

chatbot()
