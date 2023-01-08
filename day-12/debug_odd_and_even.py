def odd_or_even():
    
    number = int( input( 'Which number do you want to check?' ) )

    if number % 2 == 0:
        return( f'This is an even number.' ) 
    else:
        return( f'This is an odd number.' )

if __name__ == '__main__':
    result = odd_or_even()
    print( result )
