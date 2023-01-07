from random import choices
from sys import exit

game_on = True
money = 0
cards = ['SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK','CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK','DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK']
card_values = [
    {'Cards':['SA','HA','CA','DA'],'Values':11},
    {'Cards':['S2','H2','C2','D2'],'Values':2},
    {'Cards':['S3','H3','C3','D3'],'Values':3},
    {'Cards':['S4','H4','C4','D4'],'Values':4},
    {'Cards':['S5','H5','C5','D5'],'Values':5},
    {'Cards':['S6','H6','C6','D6'],'Values':6},
    {'Cards':['S7','H7','C7','D7'],'Values':7},
    {'Cards':['S8','H8','C8','D8'],'Values':8},
    {'Cards':['S9','H9','C9','D9'],'Values':9},
    {'Cards':['S10','H10','C10','D10','SJ','HJ','CJ','DJ','SQ','HQ','CQ','DQ','SK','HK','CK','DK'],'Values':10}
]

def purchase_chips() -> tuple[float, float]:
    if money == 0:
        chips = float( input( 'How much chips do you want to buy?:\n $') )
        bet = float( input( 'How much do you want to bet?:\n $' ) )
        return chips, bet
    else:
        bet = float( input( 'How much do you want to bet?:\n $' ) )
        return money, bet

    

def deal_cards(money:float, bet:float) -> tuple[float,float]:
    
    player_turn = True
    dealer_turn = True
    player_cards = []
    dealer_cards = []
    
    card = return_cards()
    player_cards.append( card )
    card = return_cards()
    player_cards.append( card )
    
    while player_turn:
        
        player_score = calculate_score( player_cards )    
        if player_score > 21:
            player_turn = False
        elif input( f' your card score is: {player_score}. Do you wish to hit or stay?\n').lower() == 'hit':
            card = return_cards()
            player_cards.append( card )
            player_score = calculate_score( player_cards )
        else:
            player_turn = False
    
    card = return_cards()
    dealer_cards.append( card )
    card = return_cards()
    dealer_cards.append( card )
    
    while dealer_turn:
        
        dealer_score = calculate_score( dealer_cards )
        if dealer_score <= 16:
            card = return_cards()
            dealer_cards.append( card )
            dealer_score = calculate_score( dealer_cards )
        else:
            dealer_turn = False
    
    result = calculate_winner(player_score, dealer_score)

    if result == 'Loses':
        money -= bet
        return money, result
    elif result == 'Wins':
        money += bet
        return money, result
    elif result == 'Draws':
        return money, result

def calculate_score(player_cards:list[str]):
    score = 0
    for card in player_cards:
        for line in card_values:
            if card in line['Cards']:
                score += line['Values']
    return score

def return_cards() -> list[str]:
    card = choices( cards, k=1)
    for c in card:
        if c in cards:
            cards.pop( cards.index( c ) )
        return c

def calculate_winner(player_score:int, dealer_score:int,) -> str:

    if player_score > 21:
        return f'Loses'
    elif dealer_score > 21:
        return f'Wins'
    elif player_score == dealer_score:
        return f'Draws'
    elif player_score > dealer_score:
        return f'Wins'
    else:
         return f'Loses'

if __name__ == '__main__':
    while game_on:
        money, bet = purchase_chips()
        winnings, result = deal_cards(money, bet)
        print(f'Player {result}, Player now has ${winnings} worth of chips left.')
        money = winnings
        if input( f'You have ${money} worth of chips, do you wish to continue? Type \'yes\' to continue or \'no\' to exit.\n').lower() == 'no':
            game_on = False
   