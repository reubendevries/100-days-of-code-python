from random import randint

def heads_or_tails():
    coin_toss = randint(0,1)
    if coin_toss == 1:
        return 'Heads'
    else:
        return 'Tails'


if __name__ == '__main__':
    result = heads_or_tails()
    print(result)