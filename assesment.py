import requests

answers_corrct = 0

response = requests.get('https://opentdb.com/api.php?amount=10&category=15&type=multiple')
questions = response.json()['results']
print(''' 
*~ ~ ~ ~ ~ ~ ~ Welcome to the Game Quiz!!~ ~ ~ ~ ~ ~ ~*
''')
for i, question in enumerate(questions):
    print(f'---------Question {i + 1}/20------------')
    print(question['question'])
    print(question['correct_answer'])
    for wrong_ans in question['incorrect_answers']:
        print(wrong_ans)

    while True:
        try:
            user_answer = input('\nWrite down which one you think is the correct answer!(spell it correctly please)\n')
            break
        except SyntaxError:
            print('You cant leave it blank')
    if user_answer == question['correct_answer']:
        answers_corrct += 1
        print('You got it right')
    else:
        print('\nThe correct answer was:')
        print(question['correct_answer'])
        
print(f'Thank you for playing my quiz, you got {answers_corrct} questions correct!')

