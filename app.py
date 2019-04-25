import random

variables = ['Rock', 'Paper', 'Siccors']
random = random.choice(variables)
opponent = random
player = False

while player == False:

    player = input('Rock, Paper, Scissors?').lower()
    print(player)
    
    if player == opponent:
        print('tie!, again?')
    elif player == 'rock':
        if opponent == 'Paper':
            print('Sorry buddy', opponent, 'Covers', player)
        else:
            print('You won!', player, 'CRUSHES', opponent, ':)')
    elif player == 'paper':
        if (opponent == 'Scissors'):
            print('Sorry buddy', opponent, 'cuts', player)
        else:
            print('You won!', player, 'WRAPS', opponent, ':)')
    elif player == 'scissors':
        if (opponent == 'Rock'):
            print('Sorry buddy', opponent, 'SMASHES', player)
        else:
            print('You won!', player, 'SLICES', opponent, ':)')
    else:
        print('You gotta pick Rock, Paper or Scissors')


