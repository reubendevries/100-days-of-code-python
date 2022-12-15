from random import choices

def conditions():
    num_of_letters = int( input( 'How many letters would you like in your password? '))
    num_of_symbols = int( input( 'How many symbols would you like in your password? '))
    num_of_numbers = int( input( 'How many numbers would you like in your password? '))

    return num_of_letters, num_of_symbols, num_of_numbers

def easy_password_generator(a,b,c):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbol = ['!','@','#','$','%','^','&','*','(',')','_','-','+','+','~','`',':',';','\"','\'','/','?','.','>',',','<']
    number = ['0','1','2','3','4','5','6','7','8','9']
    alpha_pass = choices(alphabet,k=a)
    symbol_pass = choices(symbol,k=b)
    number_pass = choices(number,k=c)
    password = ''
    result = alpha_pass + symbol_pass + number_pass
    for i in result:
        password += i
    return password

def hard_password_generator(a,b,c):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbol = ['!','@','#','$','%','^','&','*','(',')','_','-','+','+','~','`',':',';','\"','\'','/','?','.','>',',','<']
    number = ['0','1','2','3','4','5','6','7','8','9']
    alpha_pass = choices(alphabet,k=a)
    symbol_pass = choices(symbol,k=b)
    number_pass = choices(number,k=c)
    sorted_pass = (alpha_pass + symbol_pass + number_pass)
    mixed_pass = ''
    for i in choices(sorted_pass,k=(a+b+c)):
        mixed_pass += i
    return mixed_pass

if __name__ == '__main__':
    n_of_letters, n_of_symbols, n_of_numbers = conditions()
    password_1 = easy_password_generator(n_of_letters,n_of_symbols,n_of_numbers)
    password_2 = hard_password_generator(n_of_letters,n_of_symbols,n_of_numbers)
    
    print(password_1)
    print(password_2)
