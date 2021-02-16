import random

while True:
    player = input('Paper, Rock or Scissors?: ')
    cpu = random.choice(['Rock', 'Paper', 'Scissors'])

    if player == cpu:
        print('Tie!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('You lose!', cpu, 'covers', player)
        else:
            print('You win!', player, 'smashes', cpu)
    elif player == 'Paper':
        if computer == 'Scissors':
            print('You lose!', cpu, 'cut', player)
        else: 
            print('You win!', player, 'covers', cpu)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You lose', cpu, 'smashes', player)
        else:
            print('You win!', player, 'cut', cpu)
    else:
        print('Unavailable command')

print('Software by Nicolás Sterzer')