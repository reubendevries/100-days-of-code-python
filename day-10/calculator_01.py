from art import logo

def addition(n1:int, n2:int) -> int:
    return n1 + n2

def subtract(n1:int, n2:int) -> int:
    return n1 - n2

def divide(n1:int, n2:int) -> int:
    return n1 / n2

def multiply(n1:int, n2:int) -> int:
    return n1 * n2

def calculate(n1:int, op:str, n2:int) -> int:
    print(logo)
    if op == '+':
        ans = addition(n1, n2)
    elif op == '-':
        ans = subtract(n1, n2)
    elif op == '/':
        ans = divide(n1, n2)
    elif op == '*':
        ans = multiply(n1, n2)
    return ans


if __name__ == '__main__':

   ans = calculate(5, '/', 2)
   print(ans)