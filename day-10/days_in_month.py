def is_leap(year:int) -> bool:
    
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 !=0:
        return False
    else:
        return True

def days_in_month(year:int, month:int) -> int:
    
    months_thirty_days = [4,6,9,11]
    if month == 2:
        ans = is_leap(year)
        if ans == True:
            return 29
        else:
            return 28
    if month in months_thirty_days:
        return 30
    else:
        return 31

if __name__ == '__main__':
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year=1904, month=2)
    print(days)
