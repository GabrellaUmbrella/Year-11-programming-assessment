import requests
import random

response = requests.get('https://opentdb.com/api.php?amount=20&category=15&type=multiple')
questions = response.json()['results']

for i, question in enumerate(questions):
    print(f'-------------Questions {i}--------------')
    print(question['question'])
    all_answers = [question['correct_answer'], question['incorrect_answers'], question['incorrect_answers'], question['incorrect_answers']]
    for answers in enumerate(all_answers):
        print(random.shuffle(answers))