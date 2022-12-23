from os import system, name

all_bids = []

def clear_screen():

    if name == 'nt':
        system('cls')
    else:
        system('clear')

def calculate_winner(all_bids:list[dict]):
    winner = {
        'Name': '',
        'Bid': 0
    }
    
    for i in all_bids:
        if i['Bid'] > winner['Bid']:
            winner['Name'] = i['Name']
            winner['Bid'] = i['Bid']
    
    print( f'The winner is { winner["Name"] } with a bid of ${ winner["Bid"] }' )

def input_bidding(all_bids:list[dict]):
    print( f'Welcome to the secret auction program.' )
    name = input( f'What is your name?: ' )
    bid_input = int( input( f'What\'s your bid?: ' ) )
    more_bidders = input( f'Are there any other bidders? Type \'yes\' or \'no\'. ' ).lower()
    
    bids = {}
    bids['Name'] = name
    bids['Bid'] = bid_input

    all_bids.append(bids)
  
    if more_bidders == 'yes':
        clear_screen()
        input_bidding(all_bids)
    else:
        calculate_winner(all_bids)

if __name__ == '__main__':
    input_bidding(all_bids)
    