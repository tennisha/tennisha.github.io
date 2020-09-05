#This program is a python implementation of the casino "carnival syle" poker card games  
#This game is being implemented by Tennisha Martin of BlackGirlsHack

#Class Deck(object):
 #   def __init__():
        
class Card:
    SUITS = ('Clubs','Diamonds','Hearts','Spades')
    RANKS = ("nope','Ace','2','3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King')

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{0} of {1}'.format(Card.RANKS[self.rank],Card.SUITS[self.suit])    

class Player (object):

    def __init__( self):
        self._cards = []
        self._chips = 100
        self._bet = 0

    def clearHand (my):
        self._cards = []

    def dealCard (my, card):
        self._cards.append(card)
