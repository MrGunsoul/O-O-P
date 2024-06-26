import mammal

class Cat(mammal.Mammal):
    def __init__(self, ID, species, name, size, weight, noise, diet, owner, lives):

        mammal.Mammal.__init__(self, ID, species, name, size, weight, noise, diet, owner)

        self.__lives=lives

    def set_lives(self,lives):
        self.__lives=lives

    def get_lives(self):
        return self.__lives
    
    def __str__(self):
        st=super().__str__()
        st += '\nlives: ' + str(self.__lives) + "\n"
        return st
    
    def purr(self):
        print ("Cats purr when they are happy")