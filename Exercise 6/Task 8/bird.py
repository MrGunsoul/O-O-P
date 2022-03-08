import animals

class Bird(animals.Animals):
    def __init__(self, ID, species, name, weight, diet, domestic, wingSpan):

        animals.Animals.__init__(self, ID, species, name, weight, diet, domestic)

        self.__wingSpan=wingSpan
        self.storage={ID:[species, name, weight, diet,domestic]}

    def setwingSpan(self,wing):
        self.__wingSpan=wing

    def getwingSpan(self):
        return self.__wingSpan
    
    def __str__(self):
        st=super().__str__()
        st += '\nWing span is: ' + str(self.__wingSpan) + "\n"
        return st
    
    def flight(self):
        print (self.__name,"is able to fly!")