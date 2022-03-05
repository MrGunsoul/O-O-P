import automobile

class SUV(automobile.Automobile):
    def __init__(self, make, model, mileage, price, pass_cap):

        automobile.Automobile.__init__(self,make, model, mileage, price)

        self.__pass_cap=pass_cap

    def set_pass_cap(self,pass_cap):
        self.__pass_cap=pass_cap

    def get_pass_cap(self):
        return self.__pass_cap
    
    def __str__(self):
        st=super().__str__()
        st += '\npassenger capacity: ' + str(self.__pass_cap)
        return st
