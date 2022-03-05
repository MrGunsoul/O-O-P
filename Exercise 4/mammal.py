class Mammal:
    def __init__(self, ID, species, name, size, weight):
        self._ID=ID
        self._species=species
        self._name=name
        self._size=size
        self._weight=weight


    def __str__(self):
        return "State of the Mammal:\nID: {0}\nSpecies: {1}\nName: {2}\nSize: {3}\nWeight: {4}".format(self._ID,self._species,self._name,self._size,self._weight)
    

    def getID(self):
        print("ID is: ", self._ID)

    def getSpecies(self):
        print("Species is: ", self._species)

    def getName(self):
        print("Name is: ", self._name)

    def getSize(self):
        print("Size is: ", self._size)

    def getWeight(self):
        print("Weight is: ", self._weight)


    


    def setID(self):
        self._ID=input("Change ID: ")

    def setSpecies(self):
        self._species=input("Change Species: ")

    def setName(self):
        self._name=input("Give new Name: ")

    def setSize(self):
        self._size=input("Set new Size: ")

    def setWeight(self):
        self._weight=input("Give new Weight: ")



