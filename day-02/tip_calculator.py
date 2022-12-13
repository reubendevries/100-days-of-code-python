def calculate_tip():
    bill_amount = float(input('Enter the amount of the total of the Resturant Bill: '))
    each_payee = float(input('How many guests should this bill be split across? '))
    return '{:.2f}'.format( ( bill_amount / each_payee ) * 1.12 )

if __name__ == '__main__':
    tip = calculate_tip()
    print(tip)