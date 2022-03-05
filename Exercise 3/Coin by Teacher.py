# Nico Kranni
# Coin 2.0
# Flipping coin by teachers method

import random

# The Coin class simulate a coin that can be flipped


class Coin:

    # The __init__ method initializes the side up data attribute with 'Heads'

    def __init__(self):
        self.sideup = "Heads"
        self.currency = "Euro"

    # The toss method generates a random number in the range of 0 through 1,
    # if the number is 0, then sideup is set to Heads,
    # otherwise sideup is set to Tails

    def toss(self):
        print("This side up currently:\n", my_coin.get_sideup())
        coin = random.randint(0, 4)
        if coin == 0:
            self.sideup = "Heads"
        if coin == 1:
            self.sideup = "Tails"
        if coin == 2:
            self.sideup = "Coin landed on the table upright!"
        if coin == 3:
            self.sideup = "You buffoon! You threw the coin to the ground and now its gone!"
        if coin == 4:
            self.sideup = "Why is coin flying up towards that weird looking hole....?"
        print("This side up now:\n", my_coin.get_sideup())
    # The get_sideup method returns the value
    # references by sideup

    def money(self):
        print("Current currency:\n", my_coin.get_currency())
        value = random.randint(0, 4)
        if value == 0:
            self.currency = "Euro"
        if value == 1:
            self.currency = "Pound"
        if value == 2:
            self.currency = "Dollar"
        if value == 3:
            self.currency = "Ruble"
        if value == 4:
            self.currency = "Yen"
        print("New currency:\n", my_coin.get_currency())
    # The get_sideup method returns the value
    # references by sideup

    def get_sideup(self):
        return self.sideup

    def get_currency(self):
        return self.currency
# The main function.


'''def main():

    # Create an object from the Coin class.

    my_coin = Coin()

    # Display the side of the coin
    print("This side up:\n", my_coin.get_sideup())
    print("This currency:\n", my_coin.get_currency())
    # Toss the coin
    my_coin.toss()
    my_coin.money()

    # Display the side of the coin
    print("This side up:\n", my_coin.get_sideup())
    print("This currency:\n", my_coin.get_currency())
'''



my_coin=Coin()

my_coin.toss()
my_coin.sideup="Test"
my_coin.toss()