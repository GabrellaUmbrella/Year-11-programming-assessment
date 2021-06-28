import random
import os

def get_integer_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)

cars = []
postions = []
for i in range(12):
    cars.append(0)

def roll_dice():
    return random.randint(1, 6)

def roll_two_dice():
    return roll_dice() + roll_dice()          

car_choice = get_integer_input('choose a car \n', f'please enter a number form 1 to {len(cars)}\n', 0, len(cars))
race_distance = get_integer_input('how far is race distance\n',' plz enter num from 5 - 15\n', 4, 16)


os.system('cls')
while len([i for i in cars if i >= 15]) < 3:
    for i, car in enumerate(cars):
        if i == car_choice - 1:
            print('\033[1;32;40m' + '-'*car + 'o=o>')
        else:
            print('\033[1;34;40m' + '-'*car + 'o=o>')
    input('\033[1;36;40m' + 'push enter to continue')
    os.system('cls')
    roll = roll_two_dice()-1
    if cars[roll] < 15:
        cars[roll] += 1
        if cars[roll] == 15:
            postions.append(roll + 1)
            
wining_car = postions[0]

print(f'car {wining_car} won!!')
if wining_car == car_choice:
    print('well done your car won!')
else:
    print('you didnt pick winning car,\nbetter luck nest time')

for i, car in enumerate(postions):
    print(f'Car number {car} came in {i + 1}')





