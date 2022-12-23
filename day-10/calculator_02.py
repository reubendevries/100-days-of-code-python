from os import system, name

from art import logo

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def addition(first_number:float, second_number:float) -> float:
    return first_number + second_number

def subtract(first_number:float, second_number:float) -> float:
    return first_number - second_number

def divide(first_number:float, second_number:float) -> float:
    return first_number / second_number

def multiply(first_number:float, second_number:float) -> float:
    return first_number * second_number

def calculate() -> float:
    
    calculate_problem = True
    first_number = float( input( f'What\'s the first number?: ' ))

    while calculate_problem:
        print(logo)
        operation = input( f'Pick an operation: ' )
        second_number = float( input( f'What\'s the second number?: ') )
        if operation == '+':
            ans = addition(first_number, second_number)
        elif operation == '-':
            ans = subtract(first_number, second_number)
        elif operation == '/':
            ans = divide(first_number, second_number)
        elif operation == '*':
            ans = multiply(first_number, second_number)
        if input( f'Type \'y\' to continue calculating with answer, or type \'n\' to see your final answer' ) == 'y':
            first_number = ans
        else:
            calculate_problem = False
    return ans
    
if __name__ == '__main__':

   ans = calculate()
   print(ans)