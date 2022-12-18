from random import choices
from requests import get
from hangman_art import stages, logo
from os import system, name



def clear_screen():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def choose_word():

    lives = 6
    index = 0
    past_guesses =[]
    clear_screen()
    print( f'{logo}' )
    chosen_word = ''
    word_list = get('https://random-word-api.herokuapp.com/word?number=40').json()    
    for i in choices( word_list ):
        chosen_word = i
    create_inital_display( chosen_word, lives, index, past_guesses )

def create_inital_display( chosen_word:str, lives:int, index:int, past_guesses:list[str] ):

    display = []
    for _ in chosen_word:
        display += '_'
    print( display )
    player_choice( display, chosen_word, lives, index, past_guesses )

def player_choice( display:list[str], chosen_word:str, lives:int, index:int, past_guesses:list[str] ):

    guess = input(' Guess a letter in the english alphabet: ').lower()
    check_letter( display, guess, chosen_word, lives, index, past_guesses )

def check_letter( display:list[str], guess:str, chosen_word:str, lives:int, index:int, past_guesses:list[str] ):

    try:
        len( display ) == len( chosen_word )
    except ValueError:
        print( f'The length of display and chosen word must match.' )
        exit(1)
    finally:
        for i in range(0, len( chosen_word ), 1):
            if guess not in chosen_word:
                past_guesses.append(guess)
                decrement_life( display, chosen_word, lives, index, stages, past_guesses )
            elif guess == chosen_word[i]:
                display[i] = guess
        check_game( display, chosen_word, lives, index, stages, past_guesses )

def check_game( display:list[str], chosen_word:str, lives:int, index:int, stages:list[str], past_guesses:list[str] ):

    print( f'{display}' )
    if '_' in display:
        player_choice( display, chosen_word, lives, index, past_guesses )
    else:
        status = 'alive'
        game_over( status, chosen_word, stages )

def decrement_life( display:list[str], chosen_word:str, lives:int, index:int, past_guesses:list[str], stages:list[str] ):
    
    if lives == 0:
        status = 'dead'
        game_over( status, chosen_word, stages )
    else:
        index -= 1
        lives -= 1
        clear_screen()
        print( f'{logo}' )
        print( f'{stages[index]}' )
        print( f'Past Guesses: {past_guesses}' )
        print( f'{display}' )
        
    player_choice( display, chosen_word, lives, index, past_guesses )

def game_over( status:str, chosen_word:str, stages:list[str] ):

    if status == 'alive':
        print( f'Congratulations, you won!' )
        exit(0)
    elif status == 'dead':
        print( f'{stages[0]}' )
        print( f'Sorry, you lose, better luck next time. The correct word was {chosen_word}' )
        exit(0)

if __name__ == '__main__':
    
    choose_word()