class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
   
    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck():
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show

        
deck = Deck()
deck.show()
