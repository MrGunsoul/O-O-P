class Mammal:

    def __init__(self, ID, species, name, size, weight):
        self.__ID=ID
        self.__species=species
        self.__name=name
        self.__size=size
        self.__weight=weight
        self.__storage=[self.__ID,self.__species,self.__name,self.__size,self.__weight]


    def __str__(self):
        return "State of the Mammal:\nID: {0}\nSpecies: {1}\nName: {2}\nSize: {3}\nWeight: {4}".format(self.__ID,self.__species,self.__name,self.__size,self.__weight)
    

    def getID(self):
        print("ID is: ", self.__ID)

    def getSpecies(self):
        print("Species is: ", self.__species)

    def getName(self):
        print("Name is: ", self.__name)

    def getSize(self):
        print("Size is: ", self.__size)

    def getWeight(self):
        print("Weight is: ", self.__weight)

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

kitty=Mammal("1","Cat","Cindy","2x5m",3000)
kitty2=Mammal("5","Cat","Mesi","2x5m",2500)
mammoth=Mammal("2", "mammoth", "Malamammoth", "10x15m", 18143694)
otter=Mammal ("3", "otter", "Otterton", "2x4m", 8200)
fennec=Mammal ("4", "fennec fox", "Finnick", "3x5m", 9000)
bear=Mammal ("6", "bear", "Koda", "8x8m", 500000)
tamarin=Mammal ("7", "emperor tamarin", "Hippiäinen", "1x1m", 100)
pallas_cat=Mammal ("8", "pallas's cat", "Hurdur", "2x5m", 4500)
camel=Mammal ("9", "camel", "Leonard", "4x5", 30000)
red_panda=Mammal ("10", "red panda", "Shifu", "3x5", 4800)
horse=Mammal ("11", "horse", "Spirit", "4x5m", 35000)
hippo=Mammal ("12", "hippopotamus", "Moto Moto", "6x6m", 1800000)

print(kitty)
