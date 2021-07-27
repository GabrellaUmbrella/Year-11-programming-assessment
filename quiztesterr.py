import requests
import random

response = requests.get('https://opentdb.com/api.php?amount=20&category=15&type=multiple')
questions = response.json()['results']

for i, question in enumerate(questions):
    print(f'-------------Questions {i + 1}--------------')
    print(question['question'])
    all_answers = question['incorrect_answers']
    all_answers.append(question['correct_answer'])
    random.shuffle(all_answers)
    print(all_answers)
