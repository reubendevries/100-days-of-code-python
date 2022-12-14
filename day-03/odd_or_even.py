num = input('Which number do you want to check? ')

def odd_or_even(a):
    if int(a) % 2 == 0:
        return 'This is an even number.'
    else:
        return 'This is an odd number.'

if __name__ == '__main__':
    ans = odd_or_even(num)
    print(ans)