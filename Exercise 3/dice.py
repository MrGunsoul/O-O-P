import random

class Dice:
    def __init__(self):
        self.__value=0
    

    def __str__(self):
        return str(self.get_value())
    
    def set_value(self, value):
        self.__value=value
    
    def get_value(self):
        return self.__value
    

    def roll_dice(self, maxium):
        self.set_value(random.randint(1,maxium))