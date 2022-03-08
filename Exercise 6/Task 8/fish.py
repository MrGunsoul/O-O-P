import animals

class Fish(animals.Animals):
    def __init__(self, ID, species, name, weight, diet, domestic, depth):

        animals.Animals.__init__(self, ID, species, name, weight, diet, domestic)

        self.__depth=depth
        self.storage={ID:[species,name,weight, diet,domestic]}

    def setdepth(self,wing):
        self.__depth=wing

    def getdepth(self):
        return self.__depth
    
    def __str__(self):
        st=super().__str__()
        st += '\nCan live deep as: ' + str(self.__depth) + "\n"
        return st
    
    def dive(self):
        print (self.__name,"is able to dive deep!")