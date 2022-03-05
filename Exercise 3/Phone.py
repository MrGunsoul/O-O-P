class CellPhone:

    def __init__(self):
        self.manufact=str(input("Enter the manufactor: "))
        self.model=str(input("Enter the model number: "))
        self.retail_price=int(input("Change price to: "))

    def setmanufact(self):
        self.manufact=str(input("Change manufactor to: "))
    
    def setmodel(self):
        self.model=str(input("Change model to: "))
    
    def setprice(self):
        self.retail_price=int(input("Change price to: "))
    
    def getmanufact(self):
        print("Manufactor is: ", self.manufact)
    
    def getmodel(self):
        print("Model is: ", self.model) 

    def getprice(self):
        print("Price is: ", self.retail_price)
    
    def info(self):
        print("Here is the data that you provided: ")
        print("Manufacturer: ", self.manufact)
        print("Model number: ", self.model)
        print("Retail price: ", self.retail_price)

phone=CellPhone()
phone.info()
