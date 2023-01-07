from random import randint

def pick_number() -> int:
    
    return randint(1,100)

def guessing_game(number:int):
    game_on = True
    if input( f'Do you want to play \'Hard\' or \'Easy\':\n').lower() == 'hard':
        turns = 5
    else:
        turns = 10
    while game_on:
        print(f'You have {turns} left.')
        guess = int( input( 'Guess a number between 1 and 100:\n ') )
        if guess < number:
            print( 'Number is Higher' )
            turns -= 1
        elif guess > number:
            print( 'Number is Lower' )
            turns -= 1
        elif guess == number:
            print(f'You got it, you guessed {guess} and the secret number was {number}, you got it with {turns} guesses left!')
            game_on = False
        else:
            turns -= 1
        if turns == 0:
            print( f'Sorry, you lose. The correct number was {number}.')
            game_on = False
    

if __name__ == '__main__':
    number = pick_number()
    guessing_game(number)
