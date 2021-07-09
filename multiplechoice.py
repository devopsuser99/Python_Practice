from question import question
question_prompts = [
    "What is S3 Used for? \n(a) Object Storage \n(b) Compute Functions \n(c) An IDE For Coding\n\n",
    "How Many pillars of the well Architected framework are there? \n(a) 3 \n(b)  4 \n(c) 5\n\n",
    "Who is the Amazon CEO? \n(a) Andrew Bel-Dean \n(b) Andy Jassy  \n(c) Jeff Bezos\n\n"

]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b"),
    
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) +  "/" + str(len(questions)) + " Correct")

run_test(questions)

