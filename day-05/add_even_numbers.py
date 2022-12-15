def add_even_numbers():
    total = 0
    for n in range(0,101,2):
        total += n
    return total

if __name__ == '__main__':
    ans = add_even_numbers()
    print(ans)