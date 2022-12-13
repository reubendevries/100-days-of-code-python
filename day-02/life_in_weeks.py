# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

def life_in_weeks(a):

    years = (90 - a)
    months = years * 12
    weeks = years * 52
    days = years * 365
    return f'You have {days} days, {weeks} weeks, and {months} months left.'



if __name__ == '__main__':
    ans = life_in_weeks(int(age))
    print(ans)