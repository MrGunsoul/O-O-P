import random

class Dice:
    def __init__(self):
        self.value=0
    

    def __str__(self):
        return str(self.get_value())
    
    def set_value(self, value):
        self.value=value
    
    def get_value(self):
        return self.value
    

    def roll_dice(self, maxium):
        self.set_value(random.randint(1,maxium))
