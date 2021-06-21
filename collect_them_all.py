from random import choice

print('''
_______________________________________________________________
*~ ~ ~ ~ ~ ~ ~ ~ Thank you for coming to the cafe ~ ~ ~ ~ ~ ~ ~*

You get a Token for buying coffee and if you get the word COFFEE 
______the you win a free coffee and muffin of your choice_______
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

''')
tokens = 0
def tokens(C, O, F, E):
    valid = False
    while valid == False:
        try:
            token = (choice(tokens))
            coffee = input('Would you like a coffee? ')
            if coffee == 'yes':
                print(f'You got the letter"{token}"')
                token += 1
            if coffee == 'no':
                print('Ok have a nice day!')
                break
        except ValueError:
            print('Error please answer with "yes" or "no"')
    if C == 1 and O == 1 and F == 2 and E == 2:
        print('Yay you got the word COFFEE!!')
        valid = True
print('thank you for shopping at the Cafe!!')




