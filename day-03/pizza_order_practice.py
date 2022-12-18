print('Welcome to Python Pizza Delivers')
size = input('What size of pizza do you want? S, M, or L ')
add_pepperoni = input('Do you want pepperoni? ')
extra_cheese = input('Do you want extra cheese? ')

def pizza_size(a):

    try:
        if a in ['S', 'M', 'L']:
            return a
    except ValueError:
        return 'Please choose a valid size.'

def pepperoni(a):

    try:
        if a in ['Y', 'N']:
            return a
    except ValueError:
        return 'In valid \'Add Pepperoni\' option. Please choose a valid option'

def cheese(a):

    try:
        if a in ['Y', 'N']:
            return a
    except ValueError:
        return 'Invalid \'Add Cheese\' option. Please choose a valid option'


def calculate_bill(a, b, c):

    price = 0
    if a == 'S':
        price += 15
    elif a == 'M':
        price += 20
    else:
        price += 25
    if (b == 'Y') and (a == 'M' or a == 'L'):
        price += 3
    elif (b == 'Y') and (a == 'S'):
        price += 2
    if c == 'Y':
        price += 1
    
    return f'Your final bill is: ${price}.'

if __name__ == '__main__':
    size_of_pizza = pizza_size(size)
    has_pepperoni = pepperoni(add_pepperoni)
    has_cheese = cheese(extra_cheese)
    total_bill = calculate_bill(size_of_pizza, has_pepperoni, has_cheese)
    print(total_bill)