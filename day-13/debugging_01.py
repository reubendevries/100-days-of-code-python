from random import randint


def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


def roll_dice():
    dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    dice_num = randint(0, 6)
    print(dice_imgs[dice_num])

def millenial_check():
    year = int(input("What's your year of birth?"))
    if year > 1980 and year < 1994:
        print("You are a millenial.")
    elif year > 1994:
        print("You are a Gen Z.")

def age_check():
    age = int( input( "How old are you?") )
    if age > 18:
        print(f"You can drive at age {age}.")

def words_per_page():

    pages = 0
    word_per_page = 0
    pages = int(input("Number of pages: "))
    word_per_page = int(input("Number of words per page: "))
    total_words = pages * word_per_page
    print(total_words)

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

if __name__ == '__main__':
    my_function()
    millenial_check()
    age_check()
    words_per_page()
    mutate([1,2,3,5,8,13])
