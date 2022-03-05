
from mammal import Mammal
class Person:
    def __init__(self,first_name,last_name,student_id):
        self.first_name=first_name
        self.last_name=last_name
        self.student_id=student_id
        self.storage={}

    
    #STR
    def __str__(self):
        for key in myStudent:
            return "\nPlayer ID: {0}\nName: {1} {2}\nDice number: {3}\n".format(key,myStudent[key][0],myStudent[key][1],myStudent[key][2])

    #Accessors
    def getFirst(self):
        print("My first name is: ", self.first_name)

    def getLast(self):
        print("My last name is: ", self.last_name)

    def getID(self):
        print(self.first_name+"'s ID is: ", self.student_id)

    def getFull(self):
        print("My name is: ", self.first_name, self.last_name)

    #Mutators
    def setFirst(self):
        self.first_name=input("Change first name to: ")

    def setLast(self):
        self.last_name=input("Change last name to: ")

    def setID(self):
        self.id=input("Set new student ID: ")

    def store(self,pet):
        self.storage={self.student_id:[self.first_name,self.last_name,pet.name,pet.species]}
    
    def studentInformation(self):
        for key in myStudent:
            print("Student ID:",key,"\nName:",myStudent[key][0],myStudent[key][1],"\nPet name:",myStudent[key][2],"\nPet species:",myStudent[key][3])
            print()

kitty=Mammal("1","Cat","Cindy","2x5m","600g")
kitty2=Mammal("5","Cat","Mesi","2x5m","500g")

Mr=Person("Nico", "Kranni", 11)
Mrs=Person("Reina", "Ketonen", 9)

Mr.store(kitty)
Mrs.store(kitty2)

myStudent={}
myStudent.update(Mr.storage)
myStudent.update(Mrs.storage)

Mr.studentInformation()

