# File:         card.py
# Author:       Nico Kranni
# Description:  Deck class

import random
import card
class Deck:
    def __init__(self):
        self.cards=[]
        self.build()
    

    def build(self):
        for suit in ["Spades","Clubs","Diamonds","Hearts"]:
            for rank in range(1,14):
                self.cards.append(card.Card(suit, rank))

    def show_deck(self):
        for c in self.cards:
            c.show_card()

    def shuffle_deck(self):
        print("Shuffling the deck....")
        for item in range(len(self.cards)-1,0,-1):
            r=random.randint(0,item)
            self.cards[item],self.cards[r] = self.cards[r], self.cards[item]

    def draw_card(self):
        return self.cards.pop()
