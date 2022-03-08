import domestic

class Cat(domestic.Domestic):
    def __init__(self, ID, species, name, size, weight, noise, diet, owner, domestic_animal, lives):

        domestic.Domestic.__init__(self, ID, species, name, size, weight, noise, diet, owner, domestic_animal)

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