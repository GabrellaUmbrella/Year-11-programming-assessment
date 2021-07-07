import requests

response = requests.get('https://opentdb.com/api.php?amount=10&category=15&type=multiple')
#response = requests.get('https://opentdb.com/api.php?amount=20&category=32&type=multiple')
#response = requests.get('https://opentdb.com/api.php?amount=20&category=31&type=multiple')
questions = response.json()['results']

for i, question in enumerate(questions):
    print(f'-------------Questions {i}--------------')
    print(question['question'])
    print(question['correct_answer'])
    for wrong_ans in question['incorrect_answers']:
        print(wrong_ans)

#import requests

#response = requests.get('https://opentdb.com/api.php?amount=20&category=31&type=multiple')
#questions = response.json()['results']

#for i, questions in enumerate(questions):
#    print(f'-------------Questions {i}--------------')
#    print(questions['question'])
#    print(questions['correct_answer'])
#    for wrong_ans in questions['incorrect_answers']:
#        print(wrong_ans)
