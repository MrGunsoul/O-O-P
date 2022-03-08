import mammal

class Domestic(mammal.Mammal):
    def __init__(self, ID, species, name, size, weight, noise, diet, owner, domestic_animal):

        mammal.Mammal.__init__(self, ID, species, name, size, weight, noise, diet, owner)

        self.__domestic_animal=domestic_animal

    def set_domestic_animal(self,domestic_animal):
        self.__domestic_animal=domestic_animal

    def get_domestic_animal(self):
        return self.__domestic_animal
    
    def __str__(self):
        st=super().__str__()
        st += '\nDomestic: ' + str(self.__domestic_animal)
        return st

    def touchy(self):
        print ("You may touch the animal")