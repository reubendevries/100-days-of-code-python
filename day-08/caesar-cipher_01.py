alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input( 'Type \'encode\' to encrypt, type \'decode\' to decrypt:\n' ).lower()
text = input( 'Type your message:\n' ).lower()
shift = int( input( 'Type the shift number:\n' ) )

def encode( text:str, shift:int ):
    new_text = ''
    for i in range(0, len( text ), 1):
        if text[ i ] in alphabet:
            j = ( alphabet.index( text[ i ] ) + shift )
            if ( j + shift ) >= 27:
                j = ( j + shift ) - 27
                new_text += alphabet[ j ]
            else:    
                new_text += alphabet[ j ]
    print( new_text )

if direction == 'encode':
    encode(text,shift)
#else:
    #decode(text,shift) #TODO
