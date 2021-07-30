import requests

response = requests.get('https://opentdb.com/api.php?amount=10&category=15&type=multiple')
#response = requests.get('https://opentdb.com/api.php?amount=20&category=32&type=multiple')
#response = requests.get('https://opentdb.com/api.php?amount=20&category=31&type=multiple')
#https://opentdb.com/api.php?amount=20&category=15&difficulty=easy&type=multiple

#https://opentdb.com/api.php?amount=20&category=32&difficulty=easy&type=multiple
questions = response.json()['results']

for i, question in enumerate(questions):
    print(f'-------------Questions {i}--------------')
    print(question['question'])
    print(question['correct_answer'])
    for wrong_ans in question['incorrect_answers']:
        print(wrong_ans)

# import requests
# import random

# response = requests.get('https://opentdb.com/api.php?amount=20&category=15&type=multiple')
# questions = response.json()['results']

# for i, question in enumerate(questions):
#     print(f'-------------Questions {i + 1}--------------')
#     print(question['question'])
#     all_answers = question['incorrect_answers']
#     all_answers.append(question['correct_answer'])
#     random.shuffle(all_answers)
#     for answers in all_answers:
#         print(answers)



