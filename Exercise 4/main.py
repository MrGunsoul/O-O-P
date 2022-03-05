# Nico Kranni
# main.py
# Used to run phone and dice together.


from Phone import CellPhone
from dice import Dice

def main():

 

    new_phone0=CellPhone("Nokia","3310","150")
    new_phone1=CellPhone("Nokia","3310","150")
    new_phone2=CellPhone("Nokia","3310","150")
    new_phone3=CellPhone("Nokia","3310","150")
    new_phone4=CellPhone("Nokia","3310","150")
    new_phone5=CellPhone("Nokia","3310","150")
    phones=[new_phone0,new_phone1,new_phone2,new_phone3,new_phone4,new_phone5]
    
    
    
    for item in range(0,6):
        phones[item].ID=item
    
    for phone in phones:
        print(phone)

    new_dice = Dice()
    new_dice.roll_dice(5)
    


    print("\n\nDice chose: ")
    print(phones[new_dice.get_value()])

 


main()
