# Nico Kranni
# Phone.py
# Used to create class CellPhone, and objects

import random
class CellPhone:

    def __init__(self,manufact,model,retail_price):
        self.manufact=manufact
        self.model=model
        self.retail_price=retail_price
        self.ID=random.randint(1,6)

    def __str__(self):
        return "Here is the data that you provided:\nManufacturer: {0}\nModel number: {1}\nRetail price: {2}\nThe ID is: {3}".format(self.manufact, self.model, self.retail_price, self.ID)



    def setID(self):
        self.ID=int(input("Change ID to: "))

    def setmanufact(self):
        self.manufact=str(input("Change manufactor to: "))
    
    def setmodel(self):
        self.model=str(input("Change model to: "))
    
    def setprice(self):
        self.retail_price=int(input("Change price to: "))
    

    def getID(self):
        self.ID=print("The ID is: ", self.ID)

    def getmanufact(self):
        print("Manufactor is: ", self.manufact)
    
    def getmodel(self):
        print("Model is: ", self.model) 

    def getprice(self):
        print("Price is: ", self.retail_price)