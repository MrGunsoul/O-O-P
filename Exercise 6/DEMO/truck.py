import automobile

class Truck(automobile.Automobile):
    def __init__(self, make, model, mileage, price, drive_type):

        automobile.Automobile.__init__(self,make, model, mileage, price)

        self.__drive_type=drive_type

    def set_drive_type(self,drive_type):
        self.__drive_type=drive_type

    def get_drive_type(self):
        return self.__drive_type
    
    def __str__(self):
        st=super().__str__()
        st += '\ndrive type: ' + str(self.__drive_type)
        return st
