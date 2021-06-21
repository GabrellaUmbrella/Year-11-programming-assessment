from random import choice
num = choice(range(1, 101))
print('''

*~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Higher OR Lower ~ ~ ~ ~ ~ ~ ~ ~ ~ ~*

welcome to higher or lower game where you have to guess the
_______________number that i am thinking__________________
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

''')
replay = input('Would you like to play? ')
while replay == 'yes':
    def get_integer_input(guess, error, low, high):
        valid = False
        while not valid:
            try:
                inpt = int(input(guess))
                if low < inpt < high:
                    return inpt
            except ValueError:
                print(error)
        if guess != num:
            print('Wrong')
            inpt = int(input(guess))
        if guess == num:
            print(f'Yes thats correct, The number was {num}')
            valid = True
    replay = input('Would you like to play again?')
imput = get_integer_input('please enetr a number from 1 to 100 ', 
                            'plz enter a whole number abuve 0 and below 100 ',
                            0, 
                            100)


