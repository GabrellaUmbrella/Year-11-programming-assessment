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

def roll_dice():
    return random.randint(1, 6)

car_choice = get_integer_input('choose a car \n', 'please enter a number form 1 to 6 \n', 0, 7)
race_distance = get_integer_input('how far is race distance\n',' plz enter num from 5 - 15\n', 4, 16)

cars = [0, 0, 0, 0, 0, 0]
os.system('cls')
while max(cars) < race_distance:
    for i, car in enumerate(cars):
        print('-'*car + '0-0>')
    input('push enter to continue')
    os.system('cls')
    cars[roll_dice()-1] += 1

wining_car = cars.index(max(cars)) + 1
print(f'car {wining_car} won!!')
if wining_car == car_choice:
    print('well done your car won!')
else:
    print('you didnt pick winner, better luck nest time6')
