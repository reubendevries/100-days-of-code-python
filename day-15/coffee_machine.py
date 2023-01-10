enough_ingredients = True

menu = [
    { 'Name': 'Espresso', 'Water': 50, 'Milk': 0, 'Coffee': 18, 'Price': 1.50 },
    { 'Name': 'Latte', 'Water': 200, 'Milk': 150, 'Coffee': 24, 'Price': 2.50 },
    { 'Name': 'Cappuccino', 'Water': 250, 'Milk': 100, 'Coffee': 24, 'Price': 3.00 }
]

report = {'Water': 300, 'Milk': 200, 'Coffee': 100, 'Money': 0}

def coffee_menu(report):
    
    order = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if order == 'espresso':
        payment(menu[0]['Price'], menu[0]['Name'], report)
        report = make_espresso(menu[0], report) 
    elif order == 'latte':
        payment(menu[1]['Price'], menu[0]['Name'], report)
        report =  make_latte(menu[1], report)
    elif order == 'make_cappucino':
        payment(menu[2]['Price'], menu[0]['Name'], report)
        report = make_cappucino(menu[2], report)
    else:
        print_report(report)

def payment(price, drink, report):
    payment_completed = False
    print( f'The price of the {drink} is ${price:.2f}' )
    while not payment_completed:
        print('Please insert coins')
        quarters = float( input( 'How many quarters?: ') )
        dimes = float( input( 'How many dimes?: ') )
        nickels = float( input( 'How many nickels?: ') )    
        pennies = float( input( 'How many pennies?: ') )
        total = round( (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2 )
        if total < price:
            amount_left = (price - total)
            print( f'You\'ve not put enough money in. Please put {amount_left:.2f} to cover the rest of the cost of the coffee' )
        else:
            payment_completed = True
    report['Money'] += price
    change = ( total - price )
    if change > 0.0:
        print( f'Here is { change:.2f } in change.' )
    else:
        print('Payment recieved, a fresh cup of coffee is being made for you.')

def make_espresso(drink, report):
    
   report['Water'] -= drink['Water']
   report['Coffee'] -= drink['Coffee']
   print( f'Enjoy your { drink["Name"] }' )
   return report

def make_latte(drink, report):
    
    report['Water'] -= drink['Water']
    report['Milk'] -= drink['Water']
    report['Coffee'] -= drink['Coffee']
    print( f'Enjoy your { drink["Name"] }' )
    return report

def make_cappucino(drink, report):
    
    report['Water'] -= drink['Water']
    report['Milk'] -= drink['Water']
    report['Coffee'] -= drink['Coffee']
    print( f'Enjoy your { drink["Name"] }' )
    return report

def resupply_coffee_machine(report):
    
    water = int( input( 'How much water (in millilitres) are in reloading the machine with?: (in mL)' ) )
    milk = int( input( 'How much milk (in millilitres) are in reloading the machine with?: ' ) )
    coffee = int( input( 'How much coffee (in grams) are in reloading the machine with?: ' ) )
    report['Water'] += water
    report['Milk'] += milk
    report['Coffee'] += water

def print_report(report):
    print(report)

if __name__ == '__main__':
    while enough_ingredients:
        coffee_menu(report)
        if report['Coffee'] < 24 or report['Water'] < 250 or report['Milk'] < 150:
                print( 'WARNING: You don\'t have enough supplies to make another drink.')
                if input( 'Do you want to resupply your Coffee Machine?: (choose \'yes\' or \'no\') ' ) == 'yes':
                    resupply_coffee_machine(report)
                else:
                    enough_ingredients = False
