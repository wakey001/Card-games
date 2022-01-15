import random


class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
# shows the value and suit of the card if called, eg "8 of hearts" 
    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck():
    def __init__(self):
        self.cards = []
        self.build()
# Builds the deck by combining the suit(s), and value(v) 
# This is then put into self.cards empty list then becomes an istance of the class Card  
    def build(self):
        for s in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
# A function to show all cards in the deck self.cards list. 
    def show(self):
        for c in self.cards:
            c.show()
#Shuffles the cards in self.cards using the fisher yates method.
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            random_num = random.randint(0, i)
            self.cards[i], self.cards[random_num] = \
                self.cards[random_num], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
# Draws a card from the deck and puts it in the Players own empty list self.hand.        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
#Shows the cards in the players hand, self.hand.    
    def showHand(self):
        for card in self.hand:
            card.show()
# Discards a the last card in self.hand.
    def discard(self):
        return self.hand.pop()


    def Play_game(self):
        pass


deck = Deck()
deck.shuffle()
deck.show()

