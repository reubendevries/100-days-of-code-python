def sum_of_string():

    number = input('Type a two digit number: ')
    for i in range(len(number)-1 ):
        return int(number[i]) + int(number[i+1])

if __name__ == '__main__':

    ans = sum_of_string()
    print(ans)
