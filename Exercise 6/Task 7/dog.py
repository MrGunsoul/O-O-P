import domestic

class Dog(domestic.Domestic):
    def __init__(self, ID, species, name, size, weight, noise, diet, owner,domestic_animal, tail_length):

        domestic.Domestic.__init__(self, ID, species, name, size, weight, noise, diet, owner,domestic_animal)

        self.__tail_length=tail_length

    def set_tail_length(self,tail_length):
        self.__tail_length=tail_length

    def get_tail_length(self):
        return self.__tail_length
    
    def __str__(self):
        st=super().__str__()
        st += '\ntail length: ' + str(self.__tail_length) + "\n"
        return st

    def bark(self):
        print ("Dogs love to bark!")