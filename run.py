from question import Question

question_prompts = [
    "What is the color of banana?\n(a) Red\n(b) Yellow\n\n",
    "What is the color of sky?\n(a) Blue\n(b) Green\n\n",
    "What is 1+1?\n(a) 2\n(b) 4\n\n",
    "How many zeroes are there in a thousand?\n(a) 2\n(b) 3\n\n"
]

questions = [Question(question_prompts[0], "b"),
             Question(question_prompts[1], "a"),
             Question(question_prompts[2], "a"),
             Question(question_prompts[3], "b")
             ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You got "+str(score)+"/"+str(len(questions))+" correct")

run_test(questions)