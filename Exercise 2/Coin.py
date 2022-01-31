#Nico Kranni
#Coin
#Flipping coin

import random

#The Coin class simulate a coin that can be flipped


class Coin:

    #The __init__ method initializes the side up data attribute with 'Heads'

    def __init__(self):
        self.amount=0
    

    def toss_coin(self):
        try:
            amount=int(input("How many times do we flip the coin? "))
            self.amount+=amount
            samples=[random.randint(0,1) for i in range(amount)]
            print(samples)

            if self.amount < 2:
                if samples[0] == 1:
                    print ("Tails")
                else:
                    print("Heads")
            
            else:
                heads=samples.count(0)
                tails=samples.count(1)
                print("Heads count %d, Tails count %d" % (heads, tails))
        except ValueError:
            print("Needs to be int")
        


my_coin=Coin()
my_coin.toss_coin()