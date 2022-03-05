# Description: Create four Dice objects and store them in a list.



import dice



def main():
    # Get a list of Dice objects.

    dice_list1=make_list()
    dice_list2=make_list()
    dice_list3=make_list()

    dices_list=[dice_list1,dice_list2,dice_list3]
    
    

    for list in dices_list:
        display_list(list)
    


    for list in dices_list:
        for item in list:
            item.roll_dice(6)
        display_list(list)
    
    sum1=0
    sum2=0
    sum3=0

    for value in range(0,roll_dices):
        sum1+=dice_list1[value].get_value()
    print("First person dices:",sum1)

    for value in range(0,roll_dices):
        sum2+=dice_list2[value].get_value()
    print("Second person dices:",sum2)

    for value in range(0,roll_dices):
        sum3+=dice_list3[value].get_value()
    print("Third person dices:",sum3)


    if sum1 > sum2 and sum1 >sum3:
        print("Person 1 wins")
    if sum2 > sum3 and sum2 >sum1:
        print("Person 2 wins")
    if sum3 > sum2 and sum3 >sum1:
        print("Person 3 wins")

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
    for count in range(1,roll_dices+1):

        # dice_list.append(dice.Dice())
        # Create a new Dice object in memory and
        # assing it to the dice variable
        new_dice = dice.Dice()


        # Add the object to the list.
        dice_list.append(new_dice)
    
    return dice_list
roll_dices=int(input("How many dices to roll? "))
main()

