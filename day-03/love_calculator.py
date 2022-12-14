print('Welcome to the Love Calculator!')
name1 = input('What is your name\n').upper()
name2 = input('What is their name?\n').upper()

def name_check(a):
    count_1 = 0
    count_2 = 0
    for i in a:
        if i in ['T','t','R','r','U','u','E','e']:
            count_1 +=1
        else:
            count_1 += 0
    for i in a:
        if i in ['L','l','O','o','V','v','E','e']:
            count_2 +=1
        else:
            count_2 += 0
    return ( str(count_1) + str(count_2) )

def love_calculator(c):
    if c < 10 or c > 90:
        return f'Your score is {c}, you go together like coke and mentos.'
    elif c < 50 and c > 40:
        return f'Your score is {c}, you are alright together.'
    else:
        return f'Your score is {c}.'

if __name__ == '__main__':
    score = name_check( ( name1 + name2 ) )
    result = love_calculator( int( score ) )
    print( result )


