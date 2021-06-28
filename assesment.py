import requests

response = requests.get('https://opentdb.com/api.php?amount=20&category=31&type=multiple')
questions = response.json()['results']

for i, questions in enumerate(questions):
    print(f'-------------Questions {i}--------------')
    print(questions['question'])
    print(questions['correct_answer'])
    for wrong_ans in questions['incorrect_answers']:
        print(wrong_ans)