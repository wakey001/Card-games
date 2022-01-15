import random


class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        ''' shows the value and suit of the card if called, eg 8 of hearts'''
        print("{} of {}".format(self.value, self.suit))


class Deck():
    def __init__(self):
        self.cards = []
        self.build()
  
    def build(self):
        '''Combines the suit(s), and value(v) and \
            put into self.cards empty list \
             then becomes an istance of the class Card'''
        for s in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        "A function to show all cards in the deck self.cards list."
        for c in self.cards:
            c.show()

    def shuffle(self):
        "Shuffles the cards in self.cards using the fisher yates method."
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
    
    def draw(self, deck):
        '''Draws a card from the deck and puts\
         it in the Players own empty list self.hand.'''
        self.hand.append(deck.drawCard())
        return self
  
    def showHand(self):
        "Shows the cards in the players hand, self.hand."
        for card in self.hand:
            card.show()

    def discard(self):
        "Discards a the last card in self.hand."
        return self.hand.pop()

    def Play_game(self):
        "Deal 26 cards to both player and computer"
        pass


deck = Deck()
#deck.shuffle()
#deck.show()
bob = Player("Bob")
"add string function for player"
cpu = Player("cpu")
"add string function for computer"
bob.draw(deck).draw(deck)
bob.showHand()
cpu.draw(deck).draw(deck)
cpu.showHand()
