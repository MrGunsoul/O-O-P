# Nico Kranni
# Coin 2.0
# Flipping coin by teachers method

import random

# The Coin class simulate a coin that can be flipped


class Coin:

    # The __init__ method initializes the side up data attribute with 'Heads'

    def __init__(self):
        self.sideup = "Heads"

    # The toss method generates a random number in the range of 0 through 1,
    # if the number is 0, then sideup is set to Heads,
    # otherwise sideup is set to Tails

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
    # The get_sideup method returns the value
    # references by sideup

    def get_sideup(self):
        return self.sideup

# The main function.


def main():

    # Create an object from the Coin class.

    my_coin = Coin()

    # Display the side of the coin
    print("This side up", my_coin.get_sideup())

    #Toss the coin
    my_coin.toss()

    # Display the side of the coin
    print("This side up", my_coin.get_sideup())

main()
