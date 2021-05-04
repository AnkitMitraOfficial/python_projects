import random

player1 = 'Ankit'
player2 = 'Ankit2'

roll_of_player1 = random.randint(1,6)
print(f'{player1} got {roll_of_player1}')

if roll_of_player1 == 6:
    extra_roll1 = random.randint(1,6)
    print(f'Extra roll for {player1} --> {extra_roll1} \n')

roll_of_player2 = random.randint(1,6)
print(f'{player2} got {roll_of_player2}')

if roll_of_player2 == 6:
    extra_roll2 = random.randint(1,6)
    print(f'Extra roll for {player2} --> {extra_roll2}')
    
if roll_of_player1 == roll_of_player2:
    print('\n')
    print("Woo! Both players got same value") 