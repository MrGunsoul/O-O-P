from operator import itemgetter


class Mammal:
    def __init__(self, ID, species, name, size, weight):
        self.ID=ID
        self.species=species
        self.name=name
        self.size=size
        self.weight=weight
        self.storage=[self.ID,self.species,self.name,self.size,self.weight]


    def __str__(self):
        return "State of the Mammal:\nID: {0}\nSpecies: {1}\nName: {2}\nSize: {3}\nWeight: {4}".format(self.ID,self.species,self.name,self.size,self.weight)
    

    def getID(self):
        print("ID is: ", self.ID)

    def getSpecies(self):
        print("Species is: ", self.species)

    def getName(self):
        print("Name is: ", self.name)

    def getSize(self):
        print("Size is: ", self.size)

    def getWeight(self):
        print("Weight is: ", self.weight)

    def setID(self):
        self.ID=input("Change ID: ")

    def setSpecies(self):
        self.species=input("Change Species: ")

    def setName(self):
        self.name=input("Give new Name: ")

    def setSize(self):
        self.size=input("Set new Size: ")

    def setWeight(self):
        self.weight=input("Give new Weight: ")

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

#List of animals
lista=[kitty.storage, kitty2.storage, mammoth.storage, otter.storage, fennec.storage, bear.storage, tamarin.storage, pallas_cat.storage, camel.storage, red_panda.storage, horse.storage, hippo.storage]
#Sort animals by weight
lista.sort(key=itemgetter(4))
