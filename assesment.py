import requests
import random

answers_corrct = 0

response = requests.get('https://opentdb.com/api.php?amount=20&category=15&type=multiple')
questions = response.json()['results']
print(''' 
*~ ~ ~ ~ ~ ~ ~ Welcome to the Game Quiz!!~ ~ ~ ~ ~ ~ ~*
''')
for i, question in enumerate(questions):
    print(f'---------Question {i + 1}/20------------')
    print(question['question'])
    all_answers = [question['correct_answer'], question['incorrect_answers'], question['incorrect_answers'], question['incorrect_answers']]
    for answers in enumerate(all_answers):
        print(random.shuffle(all_answers))
    while True:
        try:
            user_answer = input('\nWrite down which one you think is the correct answer!(spell it correctly please)\n')
            break
        except ValueError or (user_answer == int or float):
            print('You cant leave it blank or put Number')
    if user_answer == question['correct_answer']:
        answers_corrct += 1
        print('\nYou got it right\n')
    else:
        print('\nThe correct answer was:')
        print(question['correct_answer'])
        
print(f'Thank you for playing my quiz, you got {answers_corrct}/20 questions correct!')


