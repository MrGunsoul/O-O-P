import mammal

class Dog(mammal.Mammal):
    def __init__(self, ID, species, name, size, weight, noise, diet, owner, tail_length):

        mammal.Mammal.__init__(self, ID, species, name, size, weight, noise, diet, owner)

        self.__tail_length=tail_length

    def set_tail_length(self,tail_length):
        self.__tail_length=tail_length

    def get_tail_length(self):
        return self.__tail_length
    
    def __str__(self):
        st=super().__str__()
        st += '\ntail_length: ' + str(self.__tail_length)
        return st