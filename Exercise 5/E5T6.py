from dice import Dice
from mammal import *
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

    def store(self,roll,name,species):
        self.storage={self.student_id:[self.first_name,self.last_name,roll,name,species]}
    
    def studentInformation(self):
        for key in myStudent:
            print("Student ID:",key,"\nName:",myStudent[key][0],myStudent[key][1],"\nRoll:",myStudent[key][2],"\nPet name:",myStudent[key][3],"\nPet species:",myStudent[key][4])
            print()


#Create students
Mr=Person("Nico", "Kranni", 11)
Mrs=Person("Reina", "Ketonen", 9)

#Create two dice
noppa1=Dice()
noppa2=Dice()


# We created empty variable to store the rolls
# Then we roll the dices and store them to sum
sum1=0
noppa1.roll_dice(6)
noppa2.roll_dice(6)
sum1+=noppa1.get_value()
sum1+=noppa2.get_value()

# We take the sum and take corresponding animal/slot from list
animal=lista[sum1-1]
Mr.store(sum1,animal[2], animal[1])

sum1=0
noppa1.roll_dice(6)
noppa2.roll_dice(6)
sum1+=noppa1.get_value()
sum1+=noppa2.get_value()
animal=lista[sum1-1]



Mrs.store(sum1,animal[2], animal[1])

myStudent={}
myStudent.update(Mr.storage) 
myStudent.update(Mrs.storage)
Mr.studentInformation()