class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
   
    def show(self):
        print("{} of {}".format(self.value, self.suit))


card = Card("Diamonds", 8)
card.show()
