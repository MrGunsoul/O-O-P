import automobile

class Car(automobile.Automobile):
    def __init__(self, make, model, mileage, price, doors):

        automobile.Automobile.__init__(self,make, model, mileage, price)

        self.__doors=doors

    def set_doors(self,doors):
        self.__doors=doors

    def get_doors(self):
        return self.__doors
    
    def __str__(self):
        st=super().__str__()
        st += '\nDoors: ' + str(self.__doors)
        return st
