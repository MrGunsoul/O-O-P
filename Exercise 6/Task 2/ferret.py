import mammal

class Ferret(mammal.Mammal):
    def __init__(self, ID, species, name, size, weight, noise, diet, owner, age):

        mammal.Mammal.__init__(self, ID, species, name, size, weight, noise, diet, owner)

        self.__age=age

    def set_age(self,age):
        self.__age=age

    def get_age(self):
        return self.__age
    
    def __str__(self):
        st=super().__str__()
        st += '\nage: ' + str(self.__age) + "\n"
        return st
    
    def jump(self):
        print ("Ferrets love to speed around and jump!")