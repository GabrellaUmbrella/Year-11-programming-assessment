from random import choice
gam = ['paper', 'scissors', 'rock']

print('''
____________________________________________________________
*~ ~ ~ ~ ~ ~ ~ ~ Paper * Scissors * Rock ~ ~ ~ ~ ~ ~ ~ ~ ~ ~*

welcome to paper, scissors, rock where you are up aginst the
________________computer to try and win______________________
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

''')
wins = 0
cwins = 0
rounds = int(input('How many rounds do you want to play? '))
rounds += 1
for i in range(rounds):
    PSR = choice(gam)
    coice = input('Choose "paper", "scissors" or "rock" ')
    if coice == 'paper' or 'scissors' or 'rock':
        if (coice == 'scissors' and PSR == 'paper') or (coice == 'paper' and PSR == 'rock') or (coice == 'rock' and PSR == 'scissors'):
            print(f'\n\nWIN!!!You chose {coice} and the computer chose {PSR}')
            wins += 1
        if coice == PSR:
            print(f'\n\nA DRAW!!!You chose {coice} and the computer chose {PSR}')
        if (coice == 'paper' and PSR == 'scissors') or (coice == 'rock' and PSR == 'paper') or (coice == 'scissors' and PSR == 'rock'):
            print(f"\n\nLOSE!!!You chose {coice} and the computer chose {PSR}")
            cwins += 1
    else:
        print('\nError!! Please enter either "paper", "scissors" or "rock"')

        
        
    
       


if wins > cwins:
    print(f"\nYOU WIN!!! You got {wins} wins and the compuer got {cwins} wins")
if wins < cwins:
    print(f"\nYOU LOSE!!! You got {wins} wins and the compuer got {cwins} wins")
if wins == cwins:
    print(f"\nA DRAW!!! You got {wins} wins and the compuer got {cwins} wins")

