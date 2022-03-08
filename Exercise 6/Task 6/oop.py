class OOP:

    def __init__(self, ID, name, age, height, weight):
        self.__ID=ID
        self.__name=name
        self.__age=age
        self.__height=height
        self.__weight=weight


    def __str__(self):
        return "Course member:\nID: {0}\nName:  {1}\nAge: {2}\nWeight: {3}\nHeight: {4}".format(self.__ID, self.__name, self.__age, self.__weight, self.__height)
    
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





