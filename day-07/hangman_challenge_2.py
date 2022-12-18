from random import choices

def choose_word():

    word_list = [ 'ardvark', 'baboon', 'camel' ]
    chosen_word = ''
    for i in choices( word_list,k=1 ):
        chosen_word += i
    return chosen_word

def create_display( word:str ):
    display = []
    for _ in word:
        display += '_'
    return display

def player_choice():

    return input(' Guess a letter in the english alphabet: ').lower()

def check_letter( guess:str, word:str ):
    new_display = []
    for char in word:
        if char == guess:
            new_display += guess
        else:
            new_display += '_'
    return new_display

if __name__ == '__main__':

    chosen_word = choose_word()
    print(f'Hint: the word is {chosen_word}') #remove after debugging completed.
    display = create_display(chosen_word)
    guess = player_choice()
    new_display = check_letter(guess, chosen_word)
    print(f'{new_display}')