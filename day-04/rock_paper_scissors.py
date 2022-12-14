from random import randint

def human_choice():

    return int(input('What do you choose? Type 0, for Rock, 1 for Paper or 2 for Scissors.\n'))

def computer_choice():

    return randint(0,2)

def scoring(c,d):

    if c == d:
        return f'Human choice of {d} and Computer choice of {d} results in a tie game.'
    elif c == 'Rock' and d != 'Paper':
        return f'Human choice of: {c} beats Computer choice of: {d}.'
    elif c == 'Paper' and d != 'Scissors':
        return f'Human choice of: {c} beats Computer choice of: {d}.'
    elif c == 'Scissors' and d != 'Rock':
        return f'Human choice of : {c} beats Computer choice of: {d}.'
    else:
        return f'Human choice of: {c} loses to Computer choice of: {d}.'
    

def rock_paper_scissors(a, b):

    if a == 0:
        player = 'Rock'
    
    elif a == 1:
        player = 'Paper'

    elif a == 2:
        player = 'Scissors'

    if b == 0:
        computer = 'Rock'

    elif b == 1:
        computer = 'Paper'

    elif b == 2:
        computer = 'Scissors'

    return scoring(player, computer)
       


if __name__ == '__main__':
    player_choice = human_choice()
    random_choice = computer_choice()
    result = rock_paper_scissors(player_choice, random_choice)
    print(result)