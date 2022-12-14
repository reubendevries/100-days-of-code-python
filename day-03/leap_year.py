year = int( input( 'Which year do you want to check? ' ) )

def leap_year(a):
    if a % 4 == 0:
        if a % 100 == 0 and a % 400 == 0:
            return 'Leap year.'
        elif a % 100 == 0:
            return 'Not leap year.'
        else:
            return 'Leap year.'
    else:
        return 'Not leap year.'    

if __name__ == '__main__':
    ans = leap_year(year)
    print(ans)