def check_leap_year():
    year = int( input( 'Which year do you want to check?' ) )

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return("Leap year.")
            else:
                return("Not leap year.")
        else:
            return("Leap year.")
    else:
        return("Not leap year.")

if __name__ == '__main__':
    ans = check_leap_year()
    print(ans)
