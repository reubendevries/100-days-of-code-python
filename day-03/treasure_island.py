from os import system, name

def clear_screen():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def win_treasure():
    
    clear_screen()
    return '''\nYou push open the Yellow Door and to your surprise you find the most beautiful\nroom full of priceless treasure, you smile knowing that you will never have to\nworry about being poor again.\n'''

def choose_door():
    
    clear_screen()
    print('''\nOnce across the Lake you find yourself in front of a strange castle,\nthis castle has three doors of equal shape and size, the only thing seperating\nthese three doors is their distinct colour.\n''')
    door_choice = input('\nPick which door you want to go through first, Red, Yellow or Blue:\n').upper()
        
    if door_choice == 'RED':
        result = death(6)

    elif door_choice == 'BLUE':
        result = death(7)

    elif door_choice == 'YELLOW':
        result = win_treasure()

    else:

        result = death(5)

    return result

def swim_or_wait():

    clear_screen()
    print('''\nYou arrive at a large lake, the ferry is 30 mins from reaching shore,\nyou can wait for the ferry or attempt to swim across the water looks calm and\nyou should be able to swim accross within 20 mins.\n''')
    swim_decision = input('\nDecide if you wish to Swim or Wait:\n').upper()

    if swim_decision == 'SWIM':
        result = death(4)

    elif swim_decision == 'WAIT':
        result = choose_door()
        
    else:
        result = death(3)
    
    return result

def death(a):
    
    clear_screen()
    
    if a == 1:
        return '\nAre you confused? Your only valid choices are to go \'Left\' or \'Right\', as a result you\'ve died.\n'
    
    elif a == 2:
        return '''\nAs you head towards the path on the right, you slip on some mude and fall into a deep hole,\nyou try to climb out, but the mud forces you back down. Soon it's night and you start to hear wild beasts\nyou close your eyes, realising soon you\'ll be someone\'s dinner and it won\'t be a pleasant death.\n'''

    elif a == 3:
        return '\nAre you confused? Your only valid choices are \'Swim\' or \'Wait\', as a result you\'ve died.\n'

    elif a == 4:
        return '''\nAs you jump into the cool, calm clear and surprisingly warm water you start to swim across the lake.\nIt's such a beatiful swim that you can't hear the villagers from the other side shout at you until it's too late\na huge troat grabs your left foot and drags you underwater where you become their family\'s lunch.\n'''

    elif a == 5:
        return '\nAre you confused? Your only valid choices are \'Red\', \'Yellow\' or \'Blue\', as a result you\'ve died.\n'

    elif a == 6:
        return '''\nYou push open the Red Door and to your surprise you find an empty room with a large fireplace\nburning a small fire. At the back of the room you see an old wooden chest, you race towards it hoping to find\nthe treasure you've been seeking, foolishly in your quickness you don't realize you\'ve trip a trigger.\nYou\'ve sprung a trap, the Red door shuts behind you and locks and the room starts to fill up with some sort\nof flamable gas, as you look towards the small fireplace you realize soon you\'ll be burned alive.\n'''
    
    elif a == 7:
        return '''\nYou push open the Blue Door and to your surprise you find an empty room with a large fireplace\nburning a small fire. At the back of the room you see an old wooden chest, you race towards it hoping to find\nthe treasure you've been seeking, foolishly in your quickness you don't realize you\'ve trip a trigger.\nYou\'ve sprung a trap, the Blue door shuts behind you and locks and a secret passage opens up, as you walk towards\nthe passage you realize a large hidieous wolf that hasn\'t eaten in awhile is escaping it\'s den. You brace\nyourself realizing you will soon be this hungry wolf\'s first meal in a while.\n'''

def treasure_hunt():
    
    clear_screen()
    print('''\nWelcome to Treasure Island.\nYour mission is to find the treasure. You come to a fork in the road.\nOne path goes left, while the other goes right.\n''')
    path_choice = input('\nType which path you would like to take: Left or Right:\n').upper()
    
    clear_screen()
    
    if path_choice == 'RIGHT':
        result = death(2)
    
    elif path_choice == 'LEFT':
        result = swim_or_wait()
    
    else:

        result = death(1)
    
    return result


if __name__ == '__main__':
    result = treasure_hunt()
    print(result)