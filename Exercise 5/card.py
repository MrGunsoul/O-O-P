# File:         card.py
# Author:       Nico Kranni
# Description:  Card class

import random
class Card:
    def __init__(self,suit,val):
        self.suit=suit
        self.value=val
    def __str__(self):
        return "Card is {} {} ".format(self.value, self.suit)
    def show_card(self):
        print("{} of {}".format(self.value, self.suit))

