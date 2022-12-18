from random import choices

def choose_word():

    word_list = [ 'ardvark', 'baboon', 'camel' ]
    chosen_word = ''
    for i in choices( word_list,k=1 ):
        chosen_word += i
    return chosen_word

def player_choice():

    return input(' Guess a letter in the english alphabet: ').lower()

def check_letter( guess:str, word:str ):
    
    for char in word:
        if char == guess:
            return f'Correct'
        else:
            return f'Incorrect'


    word = choose_word()
    char = player_choice()
    ans = check_letter(char, word)
    print(ans)
