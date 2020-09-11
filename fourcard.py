#This program is a python implementation of the casino "carnival syle" poker card games  
#This game is being implemented by Tennisha Martin of BlackGirlsHack

print ('Hello World')




class Card:
    SUITS = ('Clubs','Diamonds','Hearts','Spades')
    RANKS = ('nope','Ace','2','3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King')

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def printcards(self):
        print( "{} of {}".format(self.rank,self.suit)    )
card = Card("Clubs","Ace")
card.printcards()
class Deck:
    def __init__(self, suit, rank):
        self.cards = []
        self.build()
 
    def build (self):
        for s in  ['Clubs','Diamonds','Hearts','Spades']:
            for r in ['Ace','2','3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']:
                self.cards.append (Card(s,r))
    
    def showcards (self):
        for c in self.cards:
                print (self)
    
class Player (object):

    def __init__( self):
        self._cards = []
        self._chips = 100
        self._bet = 0

    def clearHand (self):
        self._cards = []

    def dealCard (self, card):
        self._cards.append(card)




print ('Hello World')
