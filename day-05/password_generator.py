from random import choices

def conditions():
    
    n_of_letters = int( input( 'How many letters would you like in your password? '))
    n_of_symbols = int( input( 'How many symbols would you like in your password? '))
    n_of_numbers = int( input( 'How many numbers would you like in your password? '))
    complex_simple = input( 'Do you want to generate a \'Simple\' or \'Complex\' password? ' ).upper()

    return n_of_letters, n_of_symbols, n_of_numbers, complex_simple

def complex_password( alpha_pass:list[str], symbol_pass:list[str], number_pass:list[str] ):
    
    sorted_pass = ( alpha_pass + symbol_pass + number_pass )
    password = ''
    for i in choices( sorted_pass, k=len( sorted_pass ) ):
        password += i

    return password

def simple_password( alpha_pass:list[str], symbol_pass:list[str], number_pass:list[str] ):

    sorted_pass = ( alpha_pass + symbol_pass + number_pass )
    password = ''
    for i in sorted_pass:
        password += i

    return password

def password_generator( n_of_letters:int, n_of_symbols:int, n_of_numbers:int, complex_simple:str ):
    
    alphabet = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
    symbol = [ '!','@','#','$','%','^','&','*','(',')','_','-','+','+','~','`',':',';','\"','\'','/','?','.','>',',','<' ]
    number = [ '0','1','2','3','4','5','6','7','8','9' ]

    alpha_pass = choices( alphabet,k=n_of_letters )
    symbol_pass = choices( symbol,k=n_of_symbols )
    number_pass = choices( number,k=n_of_numbers )

    if complex_simple == 'SIMPLE':
        password = simple_password( alpha_pass,symbol_pass,number_pass )

    elif complex_simple == 'COMPLEX':
        password = complex_password( alpha_pass,symbol_pass,number_pass )

    else:
        print( f'{ complex_simple } is an invalid option, please use either \'Complex\' or \'Simple\'' )
        exit()

    return password

if __name__ == '__main__':

    n_of_letters, n_of_symbols, n_of_numbers, complex_simple = conditions()

    password = password_generator( n_of_letters, n_of_symbols, n_of_numbers, complex_simple )
    
    print(f'You generated Password: { password }')
