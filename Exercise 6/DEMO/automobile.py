class Automobile:

    def __init__(self, make, model,mileage,price):
        self.__make=make
        self.__model=model
        self.__mileage=mileage
        self.__price=price
    
    #Setters
    def set_make(self,make):
        self.__make=make
    def set_model(self,model):
        self.__model=model
    def set_mileage(self,mileage):
        self.__mileage=mileage
    def set_price(self,price):
        self.__price=price
    #Getters
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price

    def __str__(self):
        return 'Make: ' + str(self.__make) + '\nModel: ' + str(self.__model) + '\nMileage: ' + str(self.__mileage) + '\nPrice: ' + str(self.__price)

        