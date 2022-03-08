import mammal

class Wild(mammal.Mammal):
    def __init__(self, ID, species, name, size, weight, noise, diet, owner, wild_animal):

        mammal.Mammal.__init__(self, ID, species, name, size, weight, noise, diet, owner)

        self.__wild_animal=wild_animal

    def set_wild_animal(self,wild_animal):
        self.__wild_animal=wild_animal

    def get_wild_animal(self):
        return self.__wild_animal
    
    def __str__(self):
        st=super().__str__()
        st += '\nWild: ' + str(self.__wild_animal)
        return st

    def noTouchy(self):
        print ("Do not touch the animal!")