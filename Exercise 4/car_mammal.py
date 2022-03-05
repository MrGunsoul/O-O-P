# Nico Kranni
# car_mammal.py
# Used to run multiple classes, car,dice,mammal

from mammal import Mammal
from car import Car
from dice import Dice

def main():

    auto=Car("Volvo","V80","534 miles","5000 €","Blue","600 kg",1)

    kitty=Mammal("0","Cat","Cindy",10,"600g")
    doggie=Mammal("1","Dog","Leevi",0.25,"1600g")
    fish=Mammal("2","fish","Golden",0.1,"60g")
    doggie2=Mammal("3","Dog","Pata",1,"1000g")
    kitty2=Mammal("4","Cat","Mesi",10,"500g")
    kitty3=Mammal("5","Cat","Bläkkis",15,"1500g")
    mammals=[kitty,doggie,fish,doggie2,kitty2,kitty3]
    
    


    new_dice = Dice()
    new_dice.roll_dice(5)
    


    print("\n\nDice chose: ")
    print(mammals[new_dice.get_value()],"\n")
    if mammals[new_dice.get_value()]._size< auto._trunk:
        print (mammals[new_dice.get_value()]._name,"fits into the car!")
    else:
        print (mammals[new_dice.get_value()]._name,"does not fit into the car!")
    


main()
