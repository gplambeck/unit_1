# Rock Paper Scissors Lizard Spock Game

# Rules:
# Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons
# Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper,
# paper disproves Spock, Spock vaporizes rock, and rock crushes scissors.

import random

# Intorduction, rules, and instructions
print('''Rock Paper Scissors Lizard Spock
\nRules: Scissors cuts paper, paper covers rock, rock crushes lizard,
lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard,
lizard eats paper, paper disproves Spock, Spock vaporizes rock, and rock
crushes scissors.
\nChoices: "r"=Rock, "p"=Paper, "s"=Scissors, "l"=Lizard, "v"=Spock''')
print()

# List of choices
selection = ['r', 'p', 's', 'l', 'v']

while True:
    p1 = input('Choose r, p, s, l, or v: ')

    # Takes care of an invalid input
    while p1 not in selection:
        p1 = input('Enter r, p, s, l, or v: ')
    print()

    # Computer randomly selects item
    p2 = random.choice(selection)
    print('Computer chose: ' + p2)
    print()
    
    # Conditions for winning
    if p1 == p2:
        print('You tie!')
    elif p1 == 'r':
        if p2 == 'p':
            print('You lose!')
        elif p2 == 's':
            print('You win!')
        elif p2 == 'l':
            print('You win!')
        else:
            print('You lose!')
    elif p1 == 'p':
        if p2 == 'r':
            print('You win!')
        elif p2 == 's':
            print('You lose!')
        elif p2 == 'l':
            print('You lose!')
        else:
            print('You win!')
    elif p1 == 's':
        if p2 == 'r':
            print('You lose!')
        elif p2 == 'p':
            print('You win!')
        elif p2 == 'l':
            print('You win!')
        else:
            print('You lose!')
    elif p1 == 'l':
        if p2 == 'r':
            print('You lose!')
        elif p2 == 'p':
            print('You win!')
        elif p2 == 's':
            print('You lose!')
        else:
            print('You win!')
    elif p1 == 'v':
        if p2 == 'r':
            print('You win!')
        elif p2 == 'p':
            print('You lose!')
        elif p2 == 's':
            print('You win!')
        else:
            print('You lose!')
    print()

    # Exiting the game
    ans_choice = ['y', 'n']
    
    answer = input('Do you want to play again? (y/n): ')

    # Takes care of an invalid answer
    while answer not in ans_choice:
        answer = input('Enter y or n: ')
    print()

    # If answer is n then break out of main while loop.
    if answer == 'n':
        break
    
# Leaving the while loop
print('\nThanks for playing!')
