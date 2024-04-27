questions = [
    "what is the capital of india",
    "mumbai is the capital of which state",
    "Which city is called silicon valley of india"
]

answers = [
    ["lucknow","delhi","himachal pradesh"],
    ["delhi","maharashtra","bangalore"],
    ["chennai","vishakapatnam","bangalore"],
]

correct_answer = ["delhi","maharashtra","bangalore"]

score = 0

def ask_questions(questions,options):

    print(questions)

    # for i,q in enumerate(questions):
    #     print(f"{i+1}.{q}")

    print()

    for i,option in enumerate(options):
        print(f"{i+1}.{option}")
    
    while True:
        try:
            choice = int(input("enter a choice from 1-4 : "))
            if choice < 1 or choice > 4:
                raise ValueError
        except ValueError:
            print("no. should be between 1 to 4 ")
        return options[choice-1]
    
for i,question in enumerate(questions):
    print(f"questions {i+1}")
    user_answer = ask_questions(questions[i],answers[i])
    if user_answer == correct_answer[i]:
        score += 1

print("result")
print(f"you scored {score} out of {len(questions)}")