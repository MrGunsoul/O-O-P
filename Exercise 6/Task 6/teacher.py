import oop

class Teacher(oop.OOP):
    def __init__(self, ID, name, age, height, weight, salary):

        oop.OOP.__init__(self, ID, name, age, height, weight)

        self.__salary=salary

    def set_salary(self,salary):
        self.__salary=salary

    def get_salary(self):
        return self.__salary
    
    def __str__(self):
        st=super().__str__()
        st += '\nsalary: ' + str(self.__salary) + "\n"
        return st
    
    def access(self):
        print ("Teachers have access to rooms")