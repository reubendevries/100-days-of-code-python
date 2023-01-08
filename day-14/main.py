from random import choices

from art import logo, vs
from game_data import data

def get_comparisons():
    score = 0
    game_on = True
    while game_on:
        compare_followers = choices( data, k=2)
        print(logo)
        print( f'Compare A: { compare_followers[0]["name"] }, a { compare_followers[0]["description"] } from { compare_followers[0]["country"] }' )
        print(vs)
        print( f'Compare B: { compare_followers[1]["name"] }, a { compare_followers[1]["description"] } from { compare_followers[1]["country"] }' )
        a_or_b = input('Who has more followers? \'A\' , \'B\' or \'Same\': ').lower()
        if compare_followers[0]['follower_count'] > compare_followers[1]['follower_count'] and a_or_b == 'a':
            score += 1
        elif compare_followers[0]['follower_count'] < compare_followers[1]['follower_count'] and a_or_b == 'b':
            score += 1
        elif compare_followers[0]['follower_count'] == compare_followers[1]['follower_count'] and a_or_b == 'same':
            score += 1
        else:
            game_on = False
    print(f' Sorry you lose, your score was {score}. Better Luck next time!')

if __name__ == '__main__':
    get_comparisons()
