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
        for c in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for i in range(1, 53):
                print(i)



deck = Deck()

