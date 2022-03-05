import random

class Card:
    def __init__(self,suit,val):
        self.suit=suit
        self.value=val
    
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards=[]
        self.build()
    

    def build(self):
        for suit in ["Spades","Clubs","Diamonds","Hearts"]:
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        print("Shuffling the deck....")
        for item in range(len(self.cards)-1,0,-1):
            r=random.randint(0,item)
            self.cards[item],self.cards[r] = self.cards[r], self.cards[item]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]

    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()
deck=Deck()
deck.show()
deck.shuffle()

steve=Player("Steve")
steve.showHand()