import oop

class Student(oop.OOP):
    def __init__(self, ID, name, age, height, weight, loan):

        oop.OOP.__init__(self, ID, name, age, height, weight)

        self.__loan=loan


    def set_loan(self,loan):
        self.__loan=loan

    def get_loan(self):
        return self.__loan
    
    def caffeine(self):
        print ("Students are fueled by pure caffeine")

    def __repr__(self):
        st=super().__repr__()
        st += '\nloan: ' + str(self.__loan) + "\n"
        return st
