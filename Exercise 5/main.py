# File:         main.py
# Author:       
# Description:  Deck of cards and card games.

import card
import deck

def main():
    
    print("Let's test that a single card works...")
    
    my_card = card.Card("Hearts", 12)
    my_card.show_card()
    print(my_card)

    print("Single card testing is over.\n")

    print("Let's test that a deck of card is created...")

    my_deck = deck.Deck()
    my_deck.show_deck()

    print("Card deck testing is over.\n")

    print("Let's shuffle the deck.")
    my_deck.shuffle_deck()

    print("Let's test that a deck of card is shuffled...")

    my_deck.show_deck()

    print("Cards should be suffled now.\n")

    print("Let's draw 2 cards and show them.")
    print("You draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    print("Your opponent draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
 
    # Code your Exercise 5 taks 7 game here. 

    #Highest of 3 game
    def game():
        # Created empty variable to store cards
        player1=0

        # Then we draw 3 cards and add it to variable
        for i in range(1,4):
            card1=my_deck.draw_card()
            player1+=card1.value
        
        player2=0
        for i in range(1,4):
            card1=my_deck.draw_card()
            player2+=card1.value
        
        player3=0
        for i in range(1,4):
            card1=my_deck.draw_card()
            player3+=card1.value
        
        # Check who has highest
        if player1 > player2 and player1 >player3:
            print("Person 1 wins")
        if player2 > player3 and player2 >player1:
            print("Person 2 wins")
        if player3 > player2 and player3 >player1:
            print("Person 3 wins")
    game()

# Calling the main function here, do not change...
main()
