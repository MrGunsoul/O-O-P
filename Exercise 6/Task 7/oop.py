class OOP:

    def __init__(self, ID, name, age, height, weight):
        self.__ID=ID
        self.__name=name
        self.__age=age
        self.__height=height
        self.__weight=weight
        self.__pet=[]
  


    def __repr__(self): 
            return self.__pet
            #return "Course member:\nID: {0}\nName:  {1}\nAge: {2}\nWeight: {3}\nHeight: {4}\nPet: {5}".format(self.__ID, self.__name, self.__age, self.__weight, self.__height, self.__pet)
   
    
    
    # Accessors
    def getID(self):
        print("ID is: ", self.__ID)
    def getName(self):
        print("Name is: ", self.__name)
    def getAge(self):
        print("Age is: ", self.__age)
    def getHeight(self):
        print("Height is: ", self.__height)
    def getWeight(self):
        print("Weight is: ", self.__weight)
    def getPet(self):
        print("First pet: ", self.__pet)



    
    
    # Mutators
    def setID(self):
        self.__ID=input("Change ID: ")
    def setName(self):
        self.__name=input("Change name: ")
    def setAge(self):
        self.__age=input("Set new age: ")
    def setHeight(self):
        self.__height=input("Set new height")
    def setWeight(self):
        self.__weight=input("Give new Weight: ")
    def setPet(self,pet):
        self.__pet.append(pet)

    def removePet(self,pet):
        self.__pet.remove(pet)
    




Mr=OOP(1, "Nico", 26, 175, 120)

