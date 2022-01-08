import random


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
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            random_num = random.randint(0, i)
            self.cards[i], self.cards[random_num] = self.cards[random_num], self.cards[i]


# deck = Deck()
# deck.show()
deck = Deck()
deck.shuffle()
deck.show()