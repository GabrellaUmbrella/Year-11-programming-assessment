import requests
import random	

answers_corrct = 0

response = requests.get('https://opentdb.com/api.php?amount=20&category=31&type=multiple')
questions = response.json()['results']
print('\033[1;36;40m' + ''' 
*~ ~ ~ ~ ~ ~ ~ Welcome to the Anime Quiz!!~ ~ ~ ~ ~ ~ ~*
''')
for i, question in enumerate(questions):
    print(f'---------Question {i + 1}/20------------')
    print(question['question'])
    all_answers = question['incorrect_answers']
    all_answers.append(question['correct_answer'])
    random.shuffle(all_answers)
    for answers in all_answers:
        print('\033[1;35;40m' + answers)

    while True:
        user_answer = input('\033[1;36;40m' + '\nWrite down which one you think is the correct answer!(spell it correctly please)\n')
        if user_answer == '':
            print('\033[1;31;40m' + "That's not a valid answer!(remember to spell it correctly)")
            print('\033[1;36;40m')
        elif user_answer in question['correct_answer']:
            answers_corrct += 1
            print('\033[1;32;40m' + '\nYou got it right ')
            print('\033[1;36;40m')
            break
        elif user_answer in question['incorrect_answers']:
            print('\033[1;33;40m' + "\nThat is incorrect, the corrct answer was")
            print(question['correct_answer'])
            print('\033[1;36;40m')
            break
        else:
            print('\033[1;31;40m' + "That's not a valid answer!(remember to spell it correctly)")
            print('\033[1;36;40m')
        
print('\033[1;35;40m' + f'Thank you for playing my quiz, you got {answers_corrct}/20 questions correct!')

