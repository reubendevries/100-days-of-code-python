from random import choices
from requests import get
from json import loads

lives = 6

def choose_word( lives:int ):

    chosen_word = ''
    word_list = get('https://random-word-api.herokuapp.com/word?number=1000').json()    
    for i in choices( word_list ):
        chosen_word = i
    create_inital_display( chosen_word, lives )

def create_inital_display( chosen_word:str, lives:int ):

    display = []
    for _ in chosen_word:
        display += '_'
    print( display )
    player_choice( display, chosen_word, lives )

def player_choice( display:list[str], chosen_word:str, lives:int ):

    guess = input(' Guess a letter in the english alphabet: ').lower()
    check_letter( display, guess, chosen_word, lives )

def check_letter( display:list[str], guess:str, chosen_word:str, lives:int ):
    try:
        len( display ) == len( chosen_word )
    except ValueError:
        print( f'The length of display and chosen word must match.' )
        exit(1)
    finally:
        for i in range(0, len( chosen_word ), 1):
            if guess not in chosen_word:
                decrement_life( display, chosen_word, lives )
            elif guess == chosen_word[i]:
                display[i] = guess
        check_game( display, chosen_word, lives )

def check_game( display:list[str], chosen_word:str, lives:int ):

    print( display )
    if '_' in display:
        player_choice( display, chosen_word, lives )
    else:
        status = 'alive'
        game_over( status, chosen_word )

def decrement_life( display:list[str], chosen_word:str, lives: int ):
    
    if lives == 0:
        status = 'dead'
        game_over( status, chosen_word )
    else:
        lives -= 1
        print( f'Sorry that\'s a wrong guess and you\'ve lost a life, be careful you only have {lives} left.' )
        player_choice( display, chosen_word, lives )

def game_over( status:str, chosen_word:str ):

    if status == 'alive':
        print( f'Congratulations, you won!' )
        exit(0)
    elif status == 'dead':
        print( f'Sorry, you lose, better luck next time. The correct word was {chosen_word}' )
        exit(0)

if __name__ == '__main__':

    choose_word( lives )