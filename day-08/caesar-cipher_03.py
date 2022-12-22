

def caesar_cipher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input( 'Type \'encode\' to encrypt, type \'decode\' to decrypt:\n' ).lower()
    text = input( 'Type your message:\n' ).lower()
    shift = int( input( 'Type the shift number:\n' ) )
    new_text = ''
    if direction == 'encode':
        for i in range(0, len( text ), 1):
            if text[ i ] in alphabet:
                j = ( alphabet.index( text[ i ] ) + shift )
                if j > 25:
                    j = j - 26
                    new_text += alphabet[ j ]
                else:    
                    new_text += alphabet[ j ]
        return new_text
    else:
        for i in range(0, len( text ), 1):
            if text[ i ] in alphabet:
                j = ( alphabet.index( text[ i ] ) - shift )
            if j < 0:
                j = j + 26
                new_text += alphabet[ j ]
            else:
                new_text += alphabet[ j ]
        return new_text

if __name__ == '__main__':
    result = caesar_cipher()
    print(result)