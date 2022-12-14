from random import randint

names_string = input('Input the name of guests seperating them by a comma: ')
names = names_string.split( ', ' )

def banker_roulette(a):
    i = randint( 0, len( a ) -1 )
    payee = a[i]

    return f'{payee} is going to buy the meal today!'


if __name__ == '__main__':
    result = banker_roulette(names)
    print(result)