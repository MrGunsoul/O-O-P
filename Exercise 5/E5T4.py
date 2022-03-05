
from dice import Dice

class Player:
    def __init__(self,first_name,last_name,player_id):
        self.first_name=first_name
        self.last_name=last_name
        self.player_id=player_id

    
    #STR
    def __str__(self):
       for key in myPlayer:
            return "\nPlayer ID: {0}\nName: {1} {2}\nDice number: {3}\n".format(key,myPlayer[key][0],myPlayer[key][1],myPlayer[key][2])

    #Accessors
    def getFirst(self):
        print("My first name is: ", self.first_name)

    def getLast(self):
        print("My last name is: ", self.last_name)

    def getID(self):
        print(self.first_name+"'s ID is: ", self.player_id)

    def getFull(self):
        print("My name is: ", self.first_name, self.last_name)

    #Mutators
    def setFirst(self):
        self.first_name=input("Change first name to: ")

    def setLast(self):
        self.last_name=input("Change last name to: ")

    def setID(self):
        self.id=input("Set new player ID: ")
    

    # Creates dictionary with player_id as key
    def store(self,dice):
        self.storage={self.player_id:[self.first_name,self.last_name,dice.value]}
    
    def playerInformation(self):
        for key in myPlayer:
            print("Player ID:",key,"\nName:",myPlayer[key][0],myPlayer[key][1],"\nDice number:",myPlayer[key][2])
            print()

# New dices and roll them
dice1=Dice()
dice2=Dice()
dice1.roll_dice(6)
dice2.roll_dice(6)

# Create players
Mr=Player("Nico","Kranni",11)
Mrs=Player("Reina","Ketonen",9)

# Create dictionary and include value of dice into it
Mr.store(dice1)
Mrs.store(dice2)

# Created empty dictionary to print players info
myPlayer={}
myPlayer.update(Mr.storage)
myPlayer.update(Mrs.storage)

Mr.playerInformation()