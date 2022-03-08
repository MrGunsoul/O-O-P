class Mammal:

    def __init__(self, ID, species, name, size, weight, noise, diet, owner):
        self.__ID=ID
        self.__species=species
        self.__name=name
        self.__size=size
        self.__weight=weight
        self.__noise=noise
        self.__diet=diet
        self.__owner=owner
        self.__storage=[self.__ID,self.__species,self.__name,self.__size,self.__weight, self.__noise, self.__diet,self.__owner]


    def __str__(self):
        return "State of the Mammal:\nID: {0}\nSpecies: {1}\nName: {2}\nSize: {3}\nWeight: {4}\nSound they make: {5}\nDiet: {6} \nOwner {7}".format(self.__ID,self.__species,self.__name,self.__size,self.__weight, self.__noise, self.__diet,self.__owner)
    
    # Accessors
    def getID(self):
        print("ID is: ", self.__ID)
    def getSpecies(self):
        print("Species is: ", self.__species)
    def getName(self):
        print("Name is: ", self.__name)
    def getSize(self):
        print("Size is: ", self.__size)
    def getNoise(self):
        print("Noise", self.__species, "makes is", self.__noise)
    def getDiet(self):
        print("Food",self.__species, "eats is : ", self.__diet)
    def getOwner(self):
        print("Owner is: ", self.__owner)
    
    
    # Mutators
    def setID(self):
        self.__ID=input("Change ID: ")
    def setSpecies(self):
        self.__species=input("Change Species: ")
    def setName(self):
        self.__name=input("Give new Name: ")
    def setSize(self):
        self.__size=input("Set new Size: ")
    def setWeight(self):
        self.__weight=input("Give new Weight: ")
    def setNoise(self):
        self.__noise=input("Give a sound")
    def setDiet(self):
        self.__diet=input("Give a food")
    def setOwner(self):
        self.__owner=input("Give a owner")

kitty=Mammal("1","Cat","Cindy","2x5m",3000, "meow", "fish","Mrs")

