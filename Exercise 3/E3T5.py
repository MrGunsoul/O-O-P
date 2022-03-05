# Nico Kranni
# Dice
# Rolling dice the game, with properties.


import random
import inspect
class Dice:

    # The __init__ method initializes the side up data attribute with 'Heads'

    def __init__(self):
        self.sideup = random.randint(1, 6) # First it gives random value for the dice
        #self.colour=str(input("Give your dice a colour: ")) # You can set color for the dice.
        self.name=str(input("Name your dice: ")) #You can name the dice when created
        #self.material=str(input("What material is your dice made of: "))


    def rematerial(self): #To change material of dice
        self.material=str(input("What material is your new material: "))
    

    def roll(self): #This rolls the dice and saves it to .sideup
        print("You roll the dice...")
        dice = random.randint(1, 6)
        self.sideup=dice
        print("This side up currently:\n", self.sideup)
    def get_sideup(self): #Gets current side that is up
        print("This side up currently:", self.sideup)




    def changeColour(self): #If you want to change colour
        self.colour=str(input("Change colour to: "))
        print ("New colour is:", self.colour)
    def getColour(self): #To check what colour you had
        print("My colour is:", self.colour)





    def changeName(self): #Change your dices name
        self.name=str(input("Give dice a new name: "))
        print("New name is: ", self.name)
    def getName(self): #Forgot what your dice name was?
        print("My name is:", self.name)
    
    def rollTheDices(self):
        first_dice.roll()
        second_dice.roll()
        print("Sum of the dices is: ", first_dice.sideup+second_dice.sideup)
    
    def theGame(self):
        print("First game:")
        
        first_dice.sideup=random.randint(1,6)
        print(first_dice.name, ":", first_dice.sideup)
       
        second_dice.sideup=random.randint(1,6)
        print(second_dice.name, ":", second_dice.sideup)
        
        third_dice.sideup=random.randint(1,6)
        print(third_dice.name, ":", third_dice.sideup)
        
        while first_dice.sideup == second_dice.sideup or first_dice.sideup==third_dice.sideup or second_dice.sideup==third_dice.sideup:
            print("Reroll")
            if first_dice.sideup == second_dice.sideup:

                first_dice.sideup= random.randint(1, 6)
                print(first_dice.name,":", first_dice.sideup)

                second_dice.sideup= random.randint(1, 6)
                print(second_dice.name,":", second_dice.sideup)
        
            if first_dice.sideup==third_dice.sideup:

                first_dice.sideup= random.randint(1, 6)
                print(first_dice.name,":", first_dice.sideup)
                
                third_dice.sideup= random.randint(1, 6)
                print(third_dice.name,":", third_dice.sideup)
        
            if second_dice.sideup==third_dice.sideup:

                third_dice.sideup= random.randint(1, 6)
                print(third_dice.name,":", third_dice.sideup)

                second_dice.sideup= random.randint(1, 6)
                print(second_dice.name,":", second_dice.sideup)


        if first_dice.sideup < second_dice.sideup and first_dice.sideup < third_dice.sideup:

            print("Second game:")
            
            second_dice.sideup=random.randint(1,6)
            print(second_dice.name, ":", second_dice.sideup)
            
            third_dice.sideup=random.randint(1,6)
            print(third_dice.name, ":", third_dice.sideup)
            

            while second_dice.sideup==third_dice.sideup:
                print("Reroll")
                if second_dice.sideup==third_dice.sideup:

                    third_dice.sideup= random.randint(1, 6)
                    print(third_dice.name,":", third_dice.sideup)

                    second_dice.sideup= random.randint(1, 6)
                    print(second_dice.name,":", second_dice.sideup)


            if second_dice.sideup < third_dice.sideup:
                print (third_dice.name, "wins!")
            else:
                print (second_dice.name, "wins!")

        if second_dice.sideup < first_dice.sideup and second_dice.sideup < third_dice.sideup:
            
            print("Second game:")
            
            first_dice.sideup=random.randint(1,6)
            print(first_dice.name, ":", first_dice.sideup)

            third_dice.sideup=random.randint(1,6)
            print(third_dice.name, ":", third_dice.sideup)
            
            while first_dice.sideup==third_dice.sideup:
                print("Reroll")
                if first_dice.sideup==third_dice.sideup:

                    first_dice.sideup= random.randint(1, 6)
                    print(first_dice.name,":", first_dice.sideup)
                
                    third_dice.sideup= random.randint(1, 6)
                    print(third_dice.name,":", third_dice.sideup)

            if first_dice.sideup < third_dice.sideup:
                print (third_dice.name, "wins!")
            else:
                print (first_dice.name, "wins!")
                       

        if third_dice.sideup < first_dice.sideup and third_dice.sideup < second_dice.sideup:
            
            print("Second game:")
            
            first_dice.sideup=random.randint(1,6)
            print(first_dice.name, ":", first_dice.sideup)
            
            second_dice.sideup=random.randint(1,6)
            print(second_dice.name, ":", second_dice.sideup)
            

            while first_dice.sideup == second_dice.sideup:
                print("Reroll")

                if first_dice.sideup == second_dice.sideup:

                    first_dice.sideup= random.randint(1, 6)
                    print(first_dice.name,":", first_dice.sideup)

                    second_dice.sideup= random.randint(1, 6)
                    print(second_dice.name,":", second_dice.sideup)

            if first_dice.sideup < second_dice.sideup:
                print (second_dice.name, "wins!")
            else:
                print (first_dice.name, "wins!",)        


 
    # The get_sideup method returns the value
    # references by sideup


first_dice=Dice()
second_dice=Dice()
third_dice=Dice()
first_dice.theGame()





