def prime_checker(number):
    count = 0
    for i in range(2,number+1,1):
        
        if number % i == 0:
            count += 1
            
    if count >= 2:
        print(f'It\'s not a prime number.')
    elif number == 1:
        print(f'It\'s not a prime number.')
    else:
        print(f'It\'s a prime number.')


if __name__ == '__main__':

    prime_checker(7)