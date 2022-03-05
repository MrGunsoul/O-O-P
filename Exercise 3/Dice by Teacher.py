# Description: Create four Dice objects and store them in a list.

import dice

def main():
    # Get a list of Dice objects.
    dice_list=make_list()
    display_list(dice_list)

    # Roll every dice once.
    for item in dice_list:
        item.roll_dice(6) #The sides on dice
    
    display_list(dice_list)

# The display_list function acceps a list containing
# objects as an argument displays the
# data stored in each object.

def display_list(a_list):
    for item in a_list:
        print(item)
    print()

def make_list():
    # Create an empty list.
    dice_list=[]

    #Add four Dice objects to the list.
    for count in range(1,5):

        # dice_list.append(dice.Dice())
        # Create a new Dice object in memory and
        # assing it to the dice variable
        new_dice = dice.Dice()


        # Add the object to the list.
        dice_list.append(new_dice)
    
    return dice_list

main()