import random
import pygame

start = input('''Welcome to the Adaptive Math test, Enter 'Start' to begin the test
>>''')
if start == 'Start':
    start_cmd = True
easy_questions = {
    "Expand: 5(x + 2)" : "5x + 10",
    "Factor: 2x^2 + 6x" : "2x(x+3)", 
}
medium_questions = {
    "Expand: (x+3)(x+7)" : "x^2+10x+21",
    "Factor: x^2 + 7x + 10" : "(x+5)(x+2)"
}
hard_questions = {
    "Expand:(3x-1)^3" : "27x^3-27x^2+9x-1",
    "Factor: x^3+3x^2-4x-12" : "(x-2)(x+2)(x+3)"
}
points = 0
correct_questions = 0
start_cmd = True
while start_cmd :
    q1 = random.choice(list(easy_questions.keys()))
    ans1 = input(q1 + " >> ")
    if ans1.replace(" ", "") == easy_questions[q1].replace(" ", ""):
        print("Correct!")
        points += 1
        correct_questions += 1
    else:
        print(f"Incorrect! The correct answer is: {easy_questions[q1]}")
    if points == 1:
        q2 = random.choice(list(medium_questions.keys()))
        ans2 = input(q2 + " >> ")
        if ans2.replace(" ", "") == medium_questions[q2].replace(" ", ""):
            print("Correct!")
            points += 1
            correct_questions += 1
        else:
            print(f"Incorrect! The correct answer is: {medium_questions[q2]}")
            points -= 1

        if points == 2:
            print('Congrats on Finishing the Quiz!')
            print(f'You got {correct_questions} correct!')
            start_cmd = False
    
