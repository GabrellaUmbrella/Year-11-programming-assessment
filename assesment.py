import requests

answrs_corct = 0

response = requests.get('https://opentdb.com/api.php?amount=10&category=15&type=multiple')
questions = response.json()['results']
print(''' 
*~ ~ ~ ~ ~ ~ ~ Welcome to the Gaming Quiz!!~ ~ ~ ~ ~ ~ ~*
\n
''')
for i, question in enumerate(questions):
    print(f'---------Question {i + 1}/20------------')
    print(question['question'])
    print(question['correct_answer'])
    for wrong_ans in question['incorrect_answers']:
        print(wrong_ans)
    user_answer = input('Write down which one you think is the correct answer!\n(spell it correctly please) ')
    if user_answer == 'correct_answer':
        answrs_corct += 1
        print('You got it right')
    print(f'The correct answer was {question['correct_answer']}')
        
print(f'Thank you for playing my quiz, you got {answrs_corct} questions correct!')

