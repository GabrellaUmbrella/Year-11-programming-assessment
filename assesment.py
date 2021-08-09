import requests
import random
from html import unescape

trys = 3
answers_corrct = 0
#This is using the users input and giving them feedback and an error message!
def get_user_inpt(all_answers):
    trys = 3
    while True:
        user_answer = input('\033[1;36;40m' + f'\nWrite down which one you think is the correct answer!(spell it correctly please, You only get {trys} try/s left!)\n')
        if user_answer.lower() in [question.lower() for question in all_answers]:
            return user_answer
        else:
            trys = trys - 1
            print('\033[1;31;40m' + f"That's not a valid answer!(remember to spell it correctly, You only get {trys} try/s left!)" + '\033[1;36;40m')
            if trys == 0:
                return "out of tries"

def check_answer(user_answer, correct_answer):
    global answers_corrct
    if user_answer == correct_answer:
        answers_corrct += 1
        print('\033[1;32;40m' + '\nYou got it right ')
        print('\033[1;36;40m')
    else:
        print('\033[1;30;40m' + "\nThat is incorrect, the corrct answer was")
        print(unescape(correct_answer))
        print('\033[1;36;40m')


#This is how i got the questions and answers into my quiz by using an API!
response = requests.get('https://opentdb.com/api.php?amount=20&category=15&difficulty=easy&type=multiple')
questions = response.json()['results']

print('\033[1;34;40m' + ''' 
*~ ~ ~ ~ ~ ~ ~ Welcome to the Game Quiz!!~ ~ ~ ~ ~ ~ ~ ~*
''')

#The block above is the code asking a question and then giving multiple answers to choose from!

for i, question in enumerate(questions):
    print('\033[1;36;40m' + f'---------Question {i + 1}/20------------')
    print(unescape(question['question']))
    all_answers = unescape(question['incorrect_answers'])
    all_answers.append(unescape(question['correct_answer']))
    random.shuffle(all_answers)
    for answers in all_answers:
        print('\033[1;35;40m' + unescape(answers))

    trys = 3
    user_answer = get_user_inpt(all_answers)
    check_answer(user_answer.lower(), question['correct_answer'].lower())
    


print('\033[1;34;40m' + f'Thank you for playing my quiz, you got {answers_corrct}/20 questions correct!')
