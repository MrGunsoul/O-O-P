class Animals:

    def __init__(self, ID, species, name, weight, diet, domestic):
        self.__ID=ID
        self.__species=species
        self.__name=name
        self.__weight=weight
        self.__diet=diet
        self.__domestic=domestic


    def __str__(self):
        return "\nState of the animal:\nID: {0}\nSpecies: {1}\nName: {2}\nWeight: {3}\nDiet: {4} \nDomestic: {5}".format(self.__ID, self.__species, self.__name,self.__weight, self.__diet, self.__domestic)
    
    # Accessors
    def getID(self):
        print("ID is: ", self.__ID)
    def getSpecies(self):
        print("Species is: ", self.__species)
    def getName(self):
        print("Name is: ", self.__name)
    def getWeight(self):
        print("Weight of animal is : ", self.__weight)
    def getDiet(self):
        print("Food",self.__species, "eats is : ", self.__diet)
    def getDomestic(self):
        print(self.__species, "is domestic: ", self.__domestic)

    
    
    # Mutators
    def setID(self):
        self.__ID=input("Change ID: ")
    def setSpecies(self):
        self.__species=input("Change Species: ")
    def setName(self):
        self.__name=input("Give new Name: ")
    def setWeight(self):
        self.__weight=input("Give new Weight: ")
    def setDiet(self):
        self.__diet=input("Give a food")
    def setDomestic(self):
        self.__domestic=input("Give true/false")


